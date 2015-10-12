# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        newHead = None

        temp = head

        while temp:
            next = temp.next
            temp.next = newHead
            newHead = temp

            temp = next

        return newHead





