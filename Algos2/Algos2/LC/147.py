# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        rVal = None
        rTail = None


        temp = head

        while temp:

            next = temp.next

            if rVal is None:
                rVal = temp
                rVal.next = None
                rTail = temp
                temp = next

                continue

            curr = rVal
            prev = None

            if rTail and rTail.val <= temp.val:
                rTail.next = temp
                temp.next = None
                rTail = temp
                continue


            # temp2 exists here
            while curr and curr.val < temp.val:
                prev = curr
                curr = curr.next

            if prev:
                prev.next = temp
                temp.next = curr

            else:

                temp.next = rVal
                rVal = temp
                

            temp = next


        return rVal








