__author__ = 'serajago'


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.length = 0
        self.currNode = None

    def add_node(self, data):
        node = Node(data)
        if self.head is None:
            self.head = node
            self.currNode = node
        else:
            self.currNode.next = node
            self.currNode = node
        self.length += 1

    def print_list(self):
        temp = self.head
        while temp:
            print("%s ->" % temp.data, end="")
            temp = temp.next


s = SinglyLinkedList()

s.add_node(10)
s.add_node(11)
s.add_node(12)
s.add_node(13)
s.print_list()


