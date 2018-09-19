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


def bfs(node, ind, dctnry):
    while node:
        if ind not in dctnry:
            dctnry[ind] = [node.val]
        else:
            dctnry[ind].append(node.val)
        if node.left:
            bfs(node.left, ind+1, dctnry)
        if node.right:
            bfs(node.right, ind+1, dctnry)
        return dctnry


if __name__ == '__main__':
    generate_tree()
    _dctnry = bfs(root, 0, {})
    for i in _dctnry:
        for j in _dctnry[i]:
            print(j)