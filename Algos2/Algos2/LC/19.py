# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        
        i = 0
        temp = head
        while i < n:
            temp = temp.next
            i += 1

        start = head
        prev = None

        while temp:
            prev = start
            start = start.next
            temp = temp.next
            

        if prev:
            prev.next = start.next

        else:
            #head has to be removed
            head = head.next



        return head



