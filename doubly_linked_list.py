class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self, data=None):
        self.head = Node(data)
        self.tail = None
        self.length = 0 if data == None else 1

    def add(self, data):
        newNode = Node(data)

        if(self.head == None):
            self.head = self.tail = newNode
            self.head.next = None
            self.tail.prev = None
        else:
            self.tail.next = newNode
            newNode.next = self.tail
            self.tail = newNode
            self.tail.prev = None

        self.length += 1
        return self

    def remove(self, index):
        # Check if index out of range
        if index >= self.length or index < self.length - (self.length * 2):
            return None
        # Convert negative index (from list end) to positive
        if index < 0:
            index = self.length + index

        # Check if head
        if index == 0:
            self.head = self.head.next
            self.head.prev = None
        # Check if tail
        elif index == self.length-1:
            self.tail = self.tail.prev
            self.tail.next = None
        else:
            curr = self.head
            while index > 0:
                curr = curr.next
                index -= 1
            curr.prev.next = curr.next
            curr.next.prev = curr.prev

        self.length -= 1
        return self

    def display(self):
        current = self.head
        if(self.head == None):
            print("List is empty")
            return
        while(current != None):
            print(current.data),
            current = current.next
