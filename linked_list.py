class LinkedList:
    def __init__(self, head=None):
        self.head = head
        self.length = 0 if head == None else 1

    def printList(self):
            current = self.head
            while current:
                print (temp.data, " -> ", end = '')
                current = current.next_node
            print("")

    def insert_head(self, data):
        new_node = Node(data)
        new_node.next_node = self.head
        self.head = new_node

    # Insert at index
    def insert(self, index, value):
        current = self.head
        if index == 0:
            return self.insert_at_head(value)
        elif index == -1:
            index = self.length - 1
        elif index >= self.length or index < -1:
            return False
        while index-1 > 0:
            current = current.next
        new_node = Node(data)
        new_node.next = current.next
        current.next = new_node
        return self.length += 1

    # Remove specified node
    def remove(self, node):
        pass

    # Remove first node with specified value
    def delete(self, value):
        pass

class Node:
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node
