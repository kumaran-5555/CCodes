__author__ = 'kumaran'

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def printList(self):
        n = self
        while(n):
            print(n.val, end=" ")
            n = n.next
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @return a ListNode
    def addTwoNumbers(self, l1, l2):
        carry = 0
        if not l1:
            return l2
        if not l2:
            return l1

        l1Cursor = l1
        l2Cursor = l2

        retHead = None
        retCursor = None

        while l1Cursor and l2Cursor:
            s = l1Cursor.val + l2Cursor.val + carry
            carry = s // 10
            s = s % 10

            l1Cursor = l1Cursor.next
            l2Cursor = l2Cursor.next

            if retCursor:
                retCursor.next = ListNode(s)
                retCursor = retCursor.next
                continue

            retCursor =  ListNode(s)
            retHead = retCursor



        # at this point at least both of them must have present,
        # and retCursor is already initialized
        while l1Cursor:
            s = l1Cursor.val + carry
            carry = s // 10
            s = s % 10
            retCursor.next = ListNode(s)
            retCursor = retCursor.next
            l1Cursor = l1Cursor.next

        while l2Cursor:
            s = l2Cursor.val + carry
            carry = s // 10
            s = s % 10
            retCursor.next = ListNode(s)
            retCursor = retCursor.next
            l2Cursor = l2Cursor.next

        if carry:
            retCursor.next = ListNode(carry)

        return retHead









if __name__ == '__main__':
    s = Solution()
    l1 = ListNode(9)
    l2 = ListNode(9)
    l2.next = ListNode(9)
    #l2.printList()
    (s.addTwoNumbers(l2, l1)).printList()
