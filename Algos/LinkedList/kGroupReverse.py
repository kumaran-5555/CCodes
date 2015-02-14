#!/usr/bin/python3
__author__ = 'kumaran'

class Node():
    def __init__(self,val):
        self.val = val
        self.next = None

    def printList(self):
        while self:
            print(self.val, end="")
            self = self.next
        print()


class Solution():
    # @param head, a ListNode
    # @param k, an integer
    # @return a ListNode
    def reverseKGroup(self, head, k):
        currHead = None
        prevTail = None
        currTail = None
        retHead = None
        count = 0
        cursor = head
        next = None

        #if k == 1:
        #    return  head

        while cursor:
            count += 1
            position = count % k


            if not currTail:
                # remember the last node in this group
                currTail = cursor

            next = cursor.next
            cursor.next = currHead
            currHead = cursor
            cursor = next

            if not position:
                # reached end of group
                if prevTail:
                    prevTail.next = currHead
                else:
                    retHead = currHead

                prevTail = currTail
                currHead = None
                currTail = None

        if count % k > 0:
            # restore the remaining sequence by reversing it
            temp = None
            while currHead:
                next = currHead.next
                currHead.next = temp
                temp = currHead
                currHead = next

            #temp.printList()
            if prevTail:
                prevTail.next = temp
            else:
                retHead = temp





        return retHead







if __name__ == '__main__':
    l = Node(1)
    l.next = Node(2)
    l.next.next = Node(3)
    l.next.next.next = Node(4)
    l.next.next.next.next = Node(5)

    s = Solution()
    s.reverseKGroup(l, 2).printList()
    
