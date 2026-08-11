depth = int(input("Enter the depth of the tree: "))

totalElements = (2 ** (depth + 1)) - 1

print("Total elements:", totalElements)

tree = []

for i in range(totalElements):
    value = input(f"Enter value for node {i + 1}: ")
    tree.append(value)

print("\nTree:", tree)

start = input("Enter start node: ")
goal = input("Enter goal node: ")


def bfs(tree, start, goal):

    startIndex = -1

    for i in range(len(tree)):
        if tree[i] == start:
            startIndex = i
            break

    if startIndex == -1:
        return [], False

    queue = [(startIndex, [start])]

    while len(queue) > 0:

        currentIndex, path = queue.pop(0)

        current = tree[currentIndex]

        if current == goal:
            return path, True

        left = 2 * currentIndex + 1
        right = 2 * currentIndex + 2

        if left < len(tree):
            queue.append((left, path + [tree[left]]))

        if right < len(tree):
            queue.append((right, path + [tree[right]]))

    return [], False


def dfs(tree, currentIndex, goal, path):

    if currentIndex >= len(tree):
        return [], False

    current = tree[currentIndex]

    path = path + [current]

    if current == goal:
        return path, True

    left = 2 * currentIndex + 1
    resultPath, found = dfs(tree, left, goal, path)

    if found:
        return resultPath, True

    right = 2 * currentIndex + 2
    resultPath, found = dfs(tree, right, goal, path)

    if found:
        return resultPath, True

    return [], False

bfsPath, bfsFound = bfs(tree, start, goal)

print("\n--- BFS ---")

if bfsFound:
    print("Goal found")
    print("Path:", " -> ".join(bfsPath))
else:
    print("Goal not found")


startIndex = -1

for i in range(len(tree)):
    if tree[i] == start:
        startIndex = i
        break

print("\n--- DFS ---")

if startIndex == -1:
    print("Start node not found")
else:
    dfsPath, dfsFound = dfs(tree, startIndex, goal, [])

    if dfsFound:
        print("Goal found")
        print("Path:", " -> ".join(dfsPath))
    else:
        print("Goal not found")