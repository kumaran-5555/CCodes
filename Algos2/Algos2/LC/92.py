# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        
        i = 1
        newHead = None
        temp = head

        firstPartTail = None


        while i < m:
            if newHead is None:
                newHead = temp

            firstPartTail = temp
            temp = temp.next
            i += 1

        reverseHead = None
        reverseTail = None

     
        while i <= n:
            next = temp.next
            temp.next = reverseHead
            reverseHead = temp

            if reverseTail is None:
                reverseTail = temp


            temp = next

            i += 1

        if reverseHead:
            reverseTail.next = temp
        else:
            reverseHead = temp

        
        if firstPartTail:
            firstPartTail.next = reverseHead
            return newHead

        return reverseHead







