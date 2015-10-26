# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        newHead = None
        prev = None
        node = head

        while node:
            if node.val == val:
                if prev:
                    prev.next = node.next
            else:
                if newHead is None:
                    newHead = node
                prev = node

            node = node.next


        return newHead


