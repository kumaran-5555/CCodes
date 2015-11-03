# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """

        if not head:
            return 

        
        slow = head
        fast = head

        while slow and fast and fast.next:
            slow = slow.next
            fast = fast.next.next


        l1 = head
        if fast:
            l2 = slow.next
        else:
            l2 = slow

        # reverse l2

        tempHead = None

        while l2:
            next = l2.next
            
            l2.next = tempHead
            tempHead = l2

            l2 = next

        # inter join l1 and tempHead
        newHead = None
        newTail = None
        while l1 and tempHead:
            n1 = l1.next
            n2 = tempHead.next
            if newHead is None:
                newHead = l1
                l1.next = tempHead
                newTail = tempHead

            else:
                newTail.next = l1
                l1.next = tempHead
                newTail = tempHead

            l1 = n1
            tempHead = n2

        if l1:
            if newTail is None:
                newHead = l1
            else:
                newTail.next = l1
                l1.next = None

        if tempHead:
            if newTail is None:
                newHead = tempHead
            else:
                newTail.next = tempHead
                tempHead.next = None

        return








