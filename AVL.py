class Node(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.height = 1

class AVL(object):
    def __init__(self, root_data=None):
        self.root = Node(root_data)

    def insert(self, data, node):
        if not node:
            node = self.root

        if not self.root:
            self.root = Node(data)
            return
        elif data < self.root.val:
            self.insert(data, node.left)
        else:
            self.insert(data, node.right)

        node.height = 1 + max(self.getHeight(node.left),
                           self.getHeight(node.right))

        balance = self.getBalance(node)

        if balance > 1 and data < node.left.val:
            return self.rightRotate(node)

        if balance < -1 and data > node.right.val:
            return self.leftRotate(node)

        if balance > 1 and data > node.left.val:
            node.left = self.leftRotate(node.left)
            return self.rightRotate(node)

        if balance < -1 and data < node.right.val:
            node.right = self.rightRotate(node.right)
            return self.leftRotate(node)

        return node

    def leftRotate(self, z):

        y = z.right
        T2 = y.left

        y.left = z
        z.right = T2

        z.height = 1 + max(self.getHeight(z.left),
                         self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left),
                         self.getHeight(y.right))

        return y

    def rightRotate(self, z):

        y = z.left
        T3 = y.right

        y.right = z
        z.left = T3

        z.height = 1 + max(self.getHeight(z.left),
                        self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left),
                        self.getHeight(y.right))

        return y

    def getHeight(self, node):
        if not node:
            return 0

        return node.height

    def getBalance(self, node):
        if not node:
            return 0

        return self.getHeight(node.left) - self.getHeight(node.right)

    def preOrder(self, node):

        if not node:
            return
