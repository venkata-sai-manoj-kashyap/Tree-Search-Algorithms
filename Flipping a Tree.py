class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def flip_tree(root):
    if not root:
        return None

    temp = root.left
    root.left = root.right
    root.right = temp

    flip_tree(root.left)
    flip_tree(root.right)

    return root


def print_tree(root):
    if not root:
        return
    print(root.val)
    if root.left:
        print("left: ", end='')
        print_tree(root.left)
    if root.right:
        print("right: ", end='')
        print_tree(root.right)


def main():
    a = TreeNode(10)
    a.left = TreeNode(20)
    a.right = TreeNode(30)
    a.left.left = TreeNode(40)
    a.left.right = TreeNode(50)

    a.right.left = TreeNode(60)
    a.right.right = TreeNode(70)
    flip_tree(a)
    print_tree(a)


if __name__ == '__main__':
    main()
