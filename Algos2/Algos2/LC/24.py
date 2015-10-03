# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        newHead = None
        newTail = None

        temp = head


        while temp and temp.next:
            
            first = temp
            second = temp.next
            
            next = second.next

            if newTail:
                newTail.next = second     
                second.next = first
                newTail = first

            else:
                second.next = first
                newTail = first
                newHead = second

            temp = next

        if temp:
            if newTail:
                newTail.next = temp
                newTail = temp
            else:
                newTail = temp
                newHead = temp

        if newTail:
            newTail.next = None


        return newHead





