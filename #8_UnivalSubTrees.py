class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

def countUnivalTreeRec(root, count):
    if not root:
        return True

    left = countUnivalTreeRec(root.left, count)
    right = countUnivalTreeRec(root.right, count)

    if not left or not right:
        return False
    if root.left and root.data != root.left.data:
        return False
    if root.right and root.data != root.right.data:
        return False

    count[0] += 1
    return True

def countUnivalTree(root):
    count = [0]
    countUnivalTreeRec(root, count)
    return count[0]


def main():
    root = Node(5)
    root.left = Node(1)
    root.right = Node(5)
    root.left.left = Node(5)
    root.left.right = Node(5)
    root.right.right = Node(5)

    print(countUnivalTree(root))

    root1 = Node(5)
    root1.left = Node(4)
    root1.right = Node(5)
    root1.left.left = Node(4)
    root1.left.right = Node(4)
    root1.right.right = Node(5)

    print(countUnivalTree(root1))

if __name__ == '__main__':
    main()
