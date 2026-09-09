import heapq

def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def astar(grid, start, goal):

    rows = len(grid)
    cols = len(grid[0])

    openList = []
    heapq.heappush(openList, (0, start))

    gCost = {start: 0}
    parent = {start: None}

    while openList:

        f, current = heapq.heappop(openList)

        if current == goal:
            path = []

            while current is not None:
                path.append(current)
                current = parent[current]

            path.reverse()
            return path

        row, col = current

        neighbours = [
            (row - 1, col),
            (row + 1, col),
            (row, col - 1),
            (row, col + 1)
        ]

        for nextNode in neighbours:

            r, c = nextNode

            if r < 0 or r >= rows or c < 0 or c >= cols:
                continue

            if grid[r][c] == 1:
                continue

            newCost = gCost[current] + 1

            if nextNode not in gCost or newCost < gCost[nextNode]:

                gCost[nextNode] = newCost

                hCost = heuristic(nextNode, goal)

                fCost = newCost + hCost

                heapq.heappush(openList, (fCost, nextNode))

                parent[nextNode] = current

    return []


rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

grid = []

print("Enter the grid using 0 for free cell and 1 for blocked cell:")

for i in range(rows):
    row = list(map(int, input().split()))
    grid.append(row)

startRow = int(input("Enter start row: "))
startCol = int(input("Enter start column: "))

goalRow = int(input("Enter goal row: "))
goalCol = int(input("Enter goal column: "))

start = (startRow, startCol)
goal = (goalRow, goalCol)

path = astar(grid, start, goal)

print("\n--- A* Search ---")

if path:
    print("Goal found")
    print("Path:")

    for node in path:
        print(node)

    print("Path length:", len(path) - 1)

else:
    print("Goal not found")
