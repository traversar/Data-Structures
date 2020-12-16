class LinkedList:
    def __init__(self, head=None):
        self.head = head
        self.length = 0 if head == None else 1

    def print_list(self):
            current = self.head
            while current:
                print (current.data, " -> ", end = '')
                current = current.next
            print("")

    def insert_head(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        self.length += 1
        return self.length

    # Insert at index
    def insert(self, index, data):
        current = self.head
        if index == 0:
            return self.insert_head(data)
        elif index == -1:
            index = self.length - 1
        elif index > self.length or index < -1:
            return False
        while index-1 > 0:
            current = current.next
            index -= 1
        new_node = Node(data)
        new_node.next = current.next
        current.next = new_node
        self.length += 1
        return self.length


    # Remove specified node
    def remove(self, node):
        current = self.head
        while current:
            if current.next == node:
                current.next, current.next.next = current.next.next, None
                self.length -= 1
                return self.length
        return False


    # Remove first node with specified data value
    def delete(self, data):
        current = self.head
        if current.data == data:
            self.head, self.head.next = current.next, None
        while current:
            if current.next.data == data:
                current.next, current.next.next = current.next.next, None
                self.length -= 1
                return self.length
        return False


class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next
