from random import randint


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def insert(self, val):
        temp = root
        while temp:
            if temp.val > val:
                if not temp.left:
                    x = TreeNode(val)
                    temp.left = x
                    return
                else:
                    temp = temp.left
            elif temp.val <= val:
                if not temp.right:
                    x = TreeNode(val)
                    temp.right = x
                    return
                else:
                    temp = temp.right


def generate_tree():
    global root
    root = TreeNode(randint(0, 100))
    for i in range(0, 100):
        root.insert(randint(0, 200))


def dfs(node):
    while node:
        print(node.val)
        if node.left:
            # print('left')
            dfs(node.left)
        if node.right:
            # print('right')
            dfs(node.right)
        # print('return')
        return


if __name__ == '__main__':
    generate_tree()
    dfs(root)
