
class Node:
    def __init__(self, value):
        self.prev = None
        self.value = value
        self.next = None

    def __str__(self):
        temp = self

        return '[{}] {} #{}[{}] -> '.format(id(temp.prev), temp.value, id(temp), id(temp.next))




class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None


    def clean(self):

        self.head = None
        self.tail = None


    def add(self, node):

        if self.tail is None:
            self.tail = node
            self.head = node
            return

        self.tail.next = node
        self.tail = node

    def addAtBegining(self, node):

        if self.head is None:
            self.tail = node
            self.head = node
            return

        node.next = self.head
        self.head = node

    def addFromList(self, list):
        self.clean()

        for i in list:
            node = Node(i)
            self.add(node)



    def deleteNode(self, node):

        temp = self.head

        if temp == node:
            self.head = node.next
            node.next = None

            return



        while temp:
            if temp.next is node:
                break
            temp = temp.next

        temp.next = node.next
        node.next = None



    
    def __str__(self):
        temp = self.head

        output = ''
        while temp:

            output +=  '[{}] {} #{}[{}] -> '.format(id(temp.prev), temp.value, id(temp), id(temp.next))

            temp = temp.next
        output += 'null'
        return output




class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add(self, node):

        if self.tail is None:
            self.tail = node
            self.head = node
            return

        self.tail.next = node
        node.prev = self.tail
        self.tail = node

    def addAtBegining(self, node):

        if self.head is None:
            self.head = node
            self.tail = node
            return


        self.head.prev = node
        node.next = self.head
        self.head = node
        return 


    def deleteNode(self, node):
        prev = node.prev 
        next = node.next


        if prev:
            prev.next = next

        if next:
            next.prev = prev

        if node is self.head:
            self.head = next

        if node is self.tail:
            self.tail = prev


        node.next = None
        node.prev = None


    def __str__(self):
        temp = self.head

        output = ''
        while temp:

            output +=  '[{}] {} #{}[{}] -> '.format(id(temp.prev), temp.value, id(temp), id(temp.next))

            temp = temp.next
        output += 'null'
        return output

    def reverse(self):

        newHead = None

        temp = self.head

        while temp:
            if newHead is None:
                newHead = temp
                temp = temp.next
                newHead.next = None

                continue

            next = temp.next

            temp.next = newHead
            newHead.prev = temp
            temp.prev = None


            newHead = temp 
            temp = next

        self.head = newHead


    def swapAlternate(self):
        newHead = None
        newTail = None

        temp = self.head


        while temp and temp.next:

            node1 = temp
            node2 = temp.next

            temp2 = temp.next.next

            node2.next = node1
            node1.prev = node2
            node1.next = None


            if newTail:
                node2.prev = newTail
                newTail.next = node2
                newTail = node1


            else:
                node2.prev = None

                newTail = node1
                newHead = node2

            temp = temp2

        if temp:
            temp.prev = newTail
            newTail.next = temp
            newTail = temp

        self.tail = newTail
        self.head = newHead




            




if __name__ == '__main__':

    l = DoublyLinkedList()
    l = LinkedList()

    l.add(Node(1))
    l.add(Node(2))
    three = Node(3)
    l.add(three)

    l.add(Node(4))
    l.add(Node(5))
    l.add(Node(6))

    print(l)
    l.deleteNode(three)
    #l.reverse()
    #l.swapAlternate()

    print(l)







