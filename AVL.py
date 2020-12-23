class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.height = 1

class AVL:
    def __init__(self, root_data=None):
        self.root = Node(root_data)

    def insert(self, data, node='empty'):
        if node == 'empty':
            if self.root:
                node = self.root
            else:
                self.root = Node(data)
                return

        if not node:
            node = Node(data)
            return
        elif data < node.val:
            if node.left == None:
                node.left = Node(data)
            else:
                self.insert(data, node.left)
        else:
            if node.right == None:
                node.right = Node(data)
            else:
                self.insert(data, node.right)

        node.height = 1 + max(self.get_height(node.left),
                           self.get_height(node.right))

        balance = self.get_balance(node)

        if balance > 1 and data < node.left.val:
            return self.right_rotate(node)

        if balance < -1 and data > node.right.val:
            return self.left_rotate(node)

        if balance > 1 and data > node.left.val:
            node.left = self.left_rotate(node.left)
            return self.right_rotate(node)

        if balance < -1 and data < node.right.val:
            node.right = self.right_rotate(node.right)
            return self.left_rotate(node)

        return self.root

    def delete(self, data, node='empty'):
        if node == 'empty':
            if self.root:
                node = self.root
            else:
                return None

        if data < node.val:
            node.left = self.delete(node.left, data)
        elif data > node.val:
            node.right = self.delete(node.right, data)
        else:
            if node.left is None:
                temp = node.right
                node = None
                return temp
            elif node.right is None:
                temp = node.left
                node = None
                return temp

            temp = self.get_min(node.right)
            node.val = temp.val
            node.right = self.delete(node.right, temp.val)

        if node is None:
            return node

        node.height = 1 + max(self.get_height(node.left), self.get_height(node.right))

        balance = self.get_balance(node)

        # If node unbalanced check four cases

        # Left Left
        if balance > 1 and self.get_balance(node.left) >= 0:
            return self.right_rotate(node)

        # Right Right
        if balance < -1 and self.get_balance(node.right) <= 0:
            return self.left_rotate(node)

        # Left Right
        if balance > 1 and self.get_balance(node.left) < 0:
            node.left = self.left_rotate(node.left)
            return self.right_rotate(node)

        # Right Left
        if balance < -1 and self.get_balance(node.right) > 0:
            node.right = self.right_rotate(node.right)
            return self.left_rotate(node)

        return node

    def left_rotate(self, z):

        y = z.right
        T2 = y.left

        y.left = z
        z.right = T2

        z.height = 1 + max(self.get_height(z.left),
                         self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left),
                         self.get_height(y.right))

        return y

    def right_rotate(self, z):

        y = z.left
        T3 = y.right

        y.right = z
        z.left = T3

        z.height = 1 + max(self.get_height(z.left),
                        self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left),
                        self.get_height(y.right))

        return y

    def get_height(self, node):
        if not node:
            return 0

        return node.height

    def get_balance(self, node):
        if not node:
            return 0

        return self.get_height(node.left) - self.get_height(node.right)

    def get_min(self, node):
        if node is None or node.left is None:
            return node

        return self.get_min(node.left)

    def inorder(self, node='empty'):
        if node == 'empty':
            node = self.root

        if not node:
            return

        self.inorder(node.left)
        print(f"{node.val} ", end='')
        self.inorder(node.right)

    def preorder(self, node='empty'):
        if node == 'empty':
            node = self.root

        if not node:
            return

        print(f"{node.val} ", end='')
        self.preorder(node.left)
        self.preorder(node.right)
