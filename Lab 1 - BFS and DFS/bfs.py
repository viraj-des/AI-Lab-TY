from collections import deque
import time

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def createTree(values, index=0):
    if index >= len(values):
        return None

    node = Node(values[index])
    node.left = createTree(values, 2 * index + 1)
    node.right = createTree(values, 2 * index + 2)

    return node


def findNode(node, value):
    if node is None:
        return None

    if node.value == value:
        return node

    result = findNode(node.left, value)

    if result:
        return result

    return findNode(node.right, value)


def bfs(root, goal):
    queue = deque([(root, [root.value])])
    visited = 0

    while queue:
        node, path = queue.popleft()
        visited += 1

        if node.value == goal:
            return path, True, visited

        if node.left:
            queue.append((node.left, path + [node.left.value]))

        if node.right:
            queue.append((node.right, path + [node.right.value]))

    return [], False, visited


def dfs(node, goal, path, visited):
    if node is None:
        return [], False, visited

    visited += 1
    path = path + [node.value]

    if node.value == goal:
        return path, True, visited

    resultPath, found, visited = dfs(node.left, goal, path, visited)

    if found:
        return resultPath, True, visited

    resultPath, found, visited = dfs(node.right, goal, path, visited)

    if found:
        return resultPath, True, visited

    return [], False, visited


depth = int(input("Enter the depth of the tree: "))

totalElements = (2 ** (depth + 1)) - 1

print("Total elements:", totalElements)

values = []

for i in range(totalElements):
    value = input(f"Enter value for node {i + 1}: ")
    values.append(value)

root = createTree(values)

start = input("Enter start node: ")
goal = input("Enter goal node: ")

startNode = findNode(root, start)

if startNode is None:
    print("Start node not found")
else:
    print("\n--- BFS ---")

    startTime = time.perf_counter()
    bfsPath, bfsFound, bfsVisited = bfs(startNode, goal)
    bfsTime = time.perf_counter() - startTime

    if bfsFound:
        print("Goal found")
        print("Path:", " -> ".join(bfsPath))
    else:
        print("Goal not found")

    print("Nodes visited:", bfsVisited)
    print("Execution time:", bfsTime, "seconds")

    print("\n--- DFS ---")

    startTime = time.perf_counter()
    dfsPath, dfsFound, dfsVisited = dfs(startNode, goal, [], 0)
    dfsTime = time.perf_counter() - startTime

    if dfsFound:
        print("Goal found")
        print("Path:", " -> ".join(dfsPath))
    else:
        print("Goal not found")

    print("Nodes visited:", dfsVisited)
    print("Execution time:", dfsTime, "seconds")

    print("\n--- Comparison ---")
    print("BFS nodes visited:", bfsVisited)
    print("DFS nodes visited:", dfsVisited)
    print("BFS time:", bfsTime, "seconds")
    print("DFS time:", dfsTime, "seconds")
