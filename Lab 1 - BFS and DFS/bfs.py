from collections import deque

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

    while queue:

        node, path = queue.popleft()

        if node.value == goal:
            return path, True

        if node.left:
            queue.append((node.left, path + [node.left.value]))

        if node.right:
            queue.append((node.right, path + [node.right.value]))

    return [], False


def dfs(node, goal, path):

    if node is None:
        return [], False

    path = path + [node.value]

    if node.value == goal:
        return path, True

    resultPath, found = dfs(node.left, goal, path)

    if found:
        return resultPath, True

    resultPath, found = dfs(node.right, goal, path)

    if found:
        return resultPath, True

    return [], False


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

    bfsPath, bfsFound = bfs(startNode, goal)

    if bfsFound:
        print("Goal found")
        print("Path:", " -> ".join(bfsPath))
    else:
        print("Goal not found")

    print("\n--- DFS ---")

    dfsPath, dfsFound = dfs(startNode, goal, [])

    if dfsFound:
        print("Goal found")
        print("Path:", " -> ".join(dfsPath))
    else:
        print("Goal not found")