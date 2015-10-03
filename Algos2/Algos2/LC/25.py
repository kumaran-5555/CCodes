# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        
        newHead = None
        newTail = None

        tempHead = None
        tempTail = None

        count = 0

        temp = head

        while temp:

            if count % k == 0 and tempHead is not None:
                # add this temporary list to permenant
                newTail.next = tempHead
                newTail = tempTail

                tempHead = None
                tempTail = None

            count += 1
            next = temp.next
            temp.next = tempHead
            tempHead = temp

            if tempTail is None:
                tempTail = temp

            temp = next


        if tempTail:
            tempTail.next = None


        if count % k > 0:
            #we have  partial list, reverse that and add to permenant

            temp = tempHead

            tempHead = None
            tempTail = None

            while temp:

                next = temp.next

                temp.next = tempHead
                tempHead = temp

                if tempTail is None:
                    tempTail = temp

                temp = next

            if newTail:
                newTail.next = tempHead
                newTail = tempTail
            else:
                newTail = tempTail
                newHead = tempHead

        if newTail:
            newTail.next = None

        return newHead



        
            

                
