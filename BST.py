class BST:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add(self, data):
        if data == self.data:
            return

        if data < self.data:
            if self.left:
                self.left.add(data)
            else:
                self.left = BST(data)
        else:
            if self.right:
                self.right.add(data)
            else:
                self.right = BST(data)

    def delete(self, data):
        if self.data is None:
            return self

        if data < self.data:
            self.left.delete(data)
        elif data > self.data:
            self.right.delete(data)
        elif data == self.data:
            if self.left is None and self.right is None:
                self.data = None
            elif self.left is None:
                self.data = self.right.data
                self.left = self.right.left
                self.right = self.right.right
                return self
            elif self.right is None:
                self.data = self.left
                self.right = self.left.right
                self.left = self.left.left
                return self

            temp = self.right.get_min()
            self.data = temp.data
            self.right.delete(temp.data)

        return self

    def find(self, val):

        if self.data == val:
            return True

        if val < self.data:
            if self.left:
                return self.left.find(val)
            else:
                return False

        if val > self.data:
            if self.right:
                return self.right.find(val)
            else:
                return False

    def get_max(self):
        if self.right is None:
            return self.data
        return self.right.get_max()

    def get_min(self):
        if self.left is None:
            return self.data
        return self.left.get_min()

    def get_sum(self):
        left_sum = self.left.get_sum() if self.left else 0
        right_sum = self.right.get_sum() if self.right else 0
        return self.data + left_sum + right_sum

    def inorder_traversal(self):
        elements = []
        if self.left:
            elements += self.left.inorder_traversal()
        elements.append(self.data)
        if self.right:
            elements += self.right.inorder_traversal()

        return elements

    def postorder_traversal(self):
        elements = []
        if self.left:
            elements += self.left.postorder_traversal()
        if self.right:
            elements += self.right.postorder_traversal()
            elements.append(self.data)

        return elements

    def preorder_traversal(self):
        elements = [self.data]
        if self.left:
            elements += self.left.preorder_traversal()
        if self.right:
            elements += self.right.preorder_traversal()

        return elements
