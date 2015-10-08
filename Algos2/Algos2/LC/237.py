# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        # assume node is not tail

        temp = node

        while temp and temp.next:
            temp.val = temp.next.val

            if not temp.next.next:
                # next node is tail
                temp.next = None

                break

            temp = temp.next

        return 


