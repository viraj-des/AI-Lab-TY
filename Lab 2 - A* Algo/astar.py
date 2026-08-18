import heapq


def a_star_graph(graph, heuristics, start, goal):
    open_set = []

    heapq.heappush(open_set, (heuristics[start], start))
    
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

        for neighbor, weight in graph[current].items():
            tentative_g = g_score[current] + weight

            if tentative_g < g_score.get(neighbor, float('inf')):
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g
                f_score = tentative_g + heuristics[neighbor]
                heapq.heappush(open_set, (f_score, neighbor))

    return None, float('inf')


graph = {
    'a': {'b': 1, 'c': 3},
    'b': {'d': 3, 'e': 1},
    'c': {'f': 5},
    'd': {'g': 2},
    'e': {'g': 1},
    'f': {'g': 2},
    'g': {}
}

heuristics = {
    'a': 5,
    'b': 3,
    'c': 4,
    'd': 2,
    'e': 1,
    'f': 2,
    'g': 0
}

start = 'f'
goal = 'g'

path, total_cost = a_star_graph(graph, heuristics, start, goal)
print(f"Path: {' -> '.join(path)}")
print(f"Total Cost: {total_cost}")