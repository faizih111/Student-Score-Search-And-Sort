scores = [250, 350, 400, 300, 500, 450, 150, 580]
if 250 in scores:
    print("Found!")
else:
    print("Not Found!")


def binarySearch(arr, targetVal):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == targetVal:
            return mid

        if arr[mid] < targetVal:
            left = mid + 1
        else:
            right = mid - 1
    return -1


x = 250

result = binarySearch(scores, x)

if result != -1:
    print("Found at index", result)
else:
    print("Not found")

n = len(scores)
for i in range(n - 1):
    for j in range(n - i - 1):
        if scores[j] > scores[j + 1]:
            scores[j], scores[j + 1] = scores[j + 1], scores[j]
print(scores)

n = len(scores)
for i in range(n - 1):
    min_index = i
    for j in range(i + 1, n):
        if scores[j] > scores[min_index]:
            min_index = j
    min_value = scores.pop(min_index)
    scores.insert(i, min_value)

print(scores)


class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def insert(node, data):
    if node is None:
        return TreeNode(data)
    else:
        if data < node.data:
            node.left = insert(node.left, data)
        elif data > node.data:
            node.right = insert(node.right, data)
        return node


def inOrderTraversal(node):
    if node is None:
        return
    inOrderTraversal(node.left)
    print(node.data, end=", ")
    inOrderTraversal(node.right)


def search(node, target):
    if node is None:
        return None
    elif node.data == target:
        return node
    elif target < node.data:
        return search(node.left, target)
    else:
        return search(node.right, target)


scores = [250, 350, 400, 300, 500, 450, 150, 580]
root = TreeNode(250)
node7 = TreeNode(350)
node15 = TreeNode(400)
node3 = TreeNode(300)
node8 = TreeNode(500)
node14 = TreeNode(450)
node19 = TreeNode(140)
node18 = TreeNode(580)

root.left = node7
root.right = node15

node7.left = node3
node7.right = node8

node15.left = node14
node15.right = node19

node19.left = node18

result = search(root, 400)
if result:
    print(f"Found the node with value: {result.data}")
else:
    print("Value not found in the BST. ")

insert(root, 600)

inOrderTraversal(root)
print("\n")


class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.height = 1


def getHeight(node):
    if not node:
        return 0
    return node.height


def getBalance(node):
    if not node:
        return 0
    return getHeight(node.left) - getHeight(node.right)


def rightRotate(y):
    print("Rotate right on node", y.data)
    x = y.left
    T2 = x.right
    x.right = y
    y.left = T2
    y.height = 1 + max(getHeight(y.left), getHeight(y.right))
    x.height = 1 + max(getHeight(x.left), getHeight(x.right))
    return x


def leftRotate(x):
    print("Rotate left on node", x.data)
    y = x.right
    T2 = y.left
    y.left = x
    x.right = T2
    x.height = 1 + max(getHeight(x.left), getHeight(x.right))
    y.height = 1 + max(getHeight(y.left), getHeight(y.right))
    return y


def insert(node, data):
    if not node:
        return TreeNode(data)

    if data < node.data:
        node.left = insert(node.left, data)
    elif data > node.data:
        node.right = insert(node.right, data)

    node.height = 1 + max(getHeight(node.left), getHeight(node.right))
    balance = getBalance(node)

    if balance > 1 and getBalance(node.left) >= 0:
        return rightRotate(node)

    if balance > 1 and getBalance(node.left) < 0:
        node.left = leftRotate(node.left)
        return rightRotate(node)

    if balance < -1 and getBalance(node.right) <= 0:
        return leftRotate(node)

    if balance < -1 and getBalance(node.right) > 0:
        node.right = rightRotate(node.right)
        return leftRotate(node)

    return node


def inOrderTraversal(node):
    if node is None:
        return
    inOrderTraversal(node.left)
    print(node.data, end=", ")
    inOrderTraversal(node.right)


root = None
for scores in scores:
    root = insert(root, scores)

inOrderTraversal(root)

my_dict_of_lists = {
    "Alice": ["Bob", "Charlie"],
    "Bob": ["Alice"],
    "Charlie": ["Alice"],
}
print("\n", my_dict_of_lists)
