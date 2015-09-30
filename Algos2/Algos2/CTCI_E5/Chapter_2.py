import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), '..') )

from LinkedList.LinkedList import LinkedList
from LinkedList.LinkedList import DoublyLinkedList
from LinkedList.LinkedList import Node


def removeDupsNoBuffer_2_1(list):

    i = list.head

    while i:
        if not i:
            break

        prev = i
        j = i.next

        while j:
            if i.value == j.value:
                # remove j, and let j point to next

                if j is list.tail:
                    list.tail = j.next


                prev.next = j.next
                j.next = None
                j = prev.next

            else:
                prev = j
                j = j.next

        i = i.next


def kThFromLast_2_2(list, k):
    # 1 - 2 - 3 - 4 - 5 - 6 - 7 - 8 - 9 - 10
    # 3rd From last is 8 
    i = list.head
    kTemp = 0
    j = None

    while i:
        i = i.next       
        kTemp += 1
        if kTemp == k:
            j = list.head
            break
        
        
    while i:
        i = i.next
        j = j.next

    return j


def deleteNode_2_3(list, node):
    list.deleteNode(node)


def partitionList_2_4(list, val):
    head1 = None
    tail1 = None
    tail2 = None
    head2 = None

    temp = list.head

    while temp:
        if temp.value < val:
            if not head1:
                head1 = temp
                tail1 = temp

            else:
                tail1.next = temp
                tail1 = temp

        else:
            if not head2:
                head2 = temp
                tail2 = temp

            else:
                tail2.next = temp
                tail2 = temp

        temp = temp.next

    if tail1:
        tail1.next = None
    if tail2:
        tail2.next = None

    if head1:
        tail1.next = head2
        list.head = head1
        list.tail = tail2

    else:
        list.head = head2
        list.tail = tail2

    
def addLinkedListNumbers_2_5(list1, list2):

    temp1 = list1.head
    temp2 = list2.head
    newHead = None
    newTail = None


    carry = 0

    while temp1 and temp2:
        s = temp1.value + temp2.value + carry

        if s > 9:
            carry = 1
            s %= 10
        
        else:
            carry = 0

        node = Node(s)

        if newTail:
            newTail.next = node
            newTail = node

        else:
            newTail = node
            newHead = node
        
        temp1 = temp1.next
        temp2 = temp2.next


    if temp1:
        temp = temp1
    elif temp2:
        temp = temp2
    else:
        temp = None


    while temp:
        s = temp.value + carry

        if s > 9:
            carry = 1
            s %= 10

        else:
            carry = 0

        node = Node(s)

        if newTail:
            newTail.next = node
            newTail = node

        else:
            newTail = node
            newHead = node
           
        temp = temp.next


    if carry > 0:
        node = None(carry)
        newTail.next = node
        newTail = node


    l = LinkedList()
    l.head = newHead
    l.tail = newTail

    return l
      
def midNode(list):

    # return tuple, (isEven, midPoint)
    slow = list.head
    fast = list.head

    while slow and fast and fast.next:
        slow = slow.next 
        fast = fast.next.next

    # if fast.next is None, it odd
    # if fast is None, it's even

    if fast is None:
        return (True, slow)

    else:
        return (False, slow)



def isPalinDrome(list):

    # one element list

    if not list.head:
        return False

    if list.head and not list.head.next:
        return True

    isEven, midPoint = midNode(list)

    # if it is odd, we need to move midPoint to next,
    # we will ingnore the midPoint for palindrome check

    if isEven is False:
        midPoint = midPoint.next

    # now midPoint points to second half of the list

    stack = []

    
    while midPoint:
        stack.append(midPoint)
        midPoint = midPoint.next


    temp = list.head

    while len(stack) and temp:
        node = stack.pop()
        if node.value != temp.value:
            return False

        temp = temp.next

    if len(stack):
        raise ValueError



    return True





if __name__ == '__main__':

    l1 = LinkedList()
    l2 = LinkedList()

    #for i in range(10,1,-1):
    #    l.add(Node(i))

    #print(l)

    #l.add(Node(10))
    #l.add(Node(2))
    #l.add(Node(11))

    #print(l)

    #removeDupsNoBuffer_2_1(l)

    #print(kThFromLast_2_2(l, 1))
    #print(kThFromLast_2_2(l, 2))
    #print(kThFromLast_2_2(l, 3))
    #print(kThFromLast_2_2(l, 100))
    #print(kThFromLast_2_2(l, 0))

    #partitionList_2_4(l, 2)

    #print(l)
    

    #l1.addFromList([7,1,6])
    #l2.addFromList([1,2,3,4,5,6,7])
    #print(l2)
    #print(addLinkedListNumbers(l1,l2))
    

    l1.addFromList([1,2,3,4,5,4,3,2,1])
    print(l1)
    print(isPalinDrome(l1))
    l1.addFromList([1,2,3,4,4,3,2,1])
    print(l1)
    print(isPalinDrome(l1))
    l1.addFromList([1,1])
    print(l1)
    print(isPalinDrome(l1))
    l1.addFromList([1])
    print(l1)
    print(isPalinDrome(l1))

    l1.addFromList([1,2])
    print(l1)
    print(isPalinDrome(l1))

    l1.addFromList([1,2,3,4,5,5,4,3,2,1,6])
    print(l1)
    print(isPalinDrome(l1))

    l1.addFromList([])
    print(l1)
    print(isPalinDrome(l1))

    print(l1)
    







