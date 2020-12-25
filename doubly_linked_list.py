class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self, data=None):
        self.head = Node(data)
        self.tail = None

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

    def display(self):
        current = self.head
        if(self.head == None):
            print("List is empty")
            return
        while(current != None):
            print(current.data),
            current = current.next
