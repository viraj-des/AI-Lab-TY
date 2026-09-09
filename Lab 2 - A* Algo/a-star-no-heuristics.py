import heapq


def heuristic(node, goal):
    return abs(node[0] - goal[0]) + abs(node[1] - goal[1])


def get_neighbors(node, rows, cols):
    r, c = node

    directions = [
        (-1, 0),
        (1, 0),
        (0, -1),
        (0, 1)
    ]

    neighbors = []

    for dr, dc in directions:
        nr = r + dr
        nc = c + dc

        if 0 <= nr < rows and 0 <= nc < cols:
            neighbors.append((nr, nc))

    return neighbors


def a_star(start, goal, rows, cols):
    open_set = []

    heapq.heappush(
        open_set,
        (heuristic(start, goal), start)
    )

    g_score = {start: 0}
    came_from = {}

    while open_set:
        _, current = heapq.heappop(open_set)

        if current == goal:
            path = []

            while current in came_from:
                path.append(current)
                current = came_from[current]

            path.append(start)

            return path[::-1], g_score[goal]

        for neighbor in get_neighbors(current, rows, cols):

            tentative_g = g_score[current] + 1

            if tentative_g < g_score.get(
                neighbor,
                float('inf')
            ):
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g

                f_score = (
                    tentative_g
                    + heuristic(neighbor, goal)
                )

                heapq.heappush(
                    open_set,
                    (f_score, neighbor)
                )

    return None, float('inf')

start = (1, 4)
goal = (7, 3)

walls = {
    
}

path, cost = a_star(start, goal, 8, 8)

print(f"Path: {path}")
print(f"Cost: {cost}")