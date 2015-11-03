# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if k == 0:
            return head
        l = 0
    
        temp = head

        while temp:
            l += 1
            temp = temp.next
        if l == 0:
            return head

        k = k%l

        if k == 0:
            return head


        temp = head
        prev = None
        i = 0
        while i < k:
            prev = temp
            temp = temp.next
            i += 1

        start = head

        while temp.next:
            start = start.next
            temp = temp.next

        newHead = start.next
        start.next = None
        temp.next = head


        return newHead



        




           

         

