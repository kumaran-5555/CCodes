# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        
        head = None
        tail = None

        temp1 = l1
        temp2 = l2

        while temp1 and temp2:
            if temp1.val <= temp2.val:
                if tail is None:
                    head = temp1
                    tail = temp1

                else:
                    tail.next = temp1
                    tail = temp1

                temp1 = temp1.next


            else:

                if tail is None:
                    head = temp2
                    tail = temp2

                else:
                    tail.next = temp2
                    tail = temp2
    
                temp2 = temp2.next

        temp = None
        if temp1 is None and temp2:
            temp = temp2

        elif temp2 is None and temp1:
            temp = temp1


        while temp:
            if tail is None:
                head = temp
                tail = temp
            else:
                tail.next = temp
                tail = temp

            temp = temp.next

        if tail:
            tail.next = None


        return head






