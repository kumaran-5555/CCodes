# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):

    def mergeList(self, h1, h2):

        head = None
        tail = None

        while h1 and h2:
            if h1.val >= h2.val:
                min = h2
                h2 = h2.next

            else:
                min = h1
                h1 = h1.next        

            if tail is None:
                tail = min
                head = min

                continue

            tail.next = min
            tail = min

        if h1:
            h = h1

        elif h2:
            h = h2

        while h:
            if tail is None:
                tail = h
                head = h

            else:
                tail.next = h
                tail = h


            h =  h.next


        if tail:
            tail.next = None

        return head

    def mergeSort(self, head):

        fast = head
        slow = head


        while fast and fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next

        if fast is slow and fast and fast.next is None:
            return head
            
        if fast is None and slow is None:
            return head

        h1 = head

        # create second list
        h2 = slow.next
        #delink frist and second
        slow.next = None

        h1 = self.mergeSort(h1)
        h2 = self.mergeSort(h2)

        return self.mergeList(h1, h2)








    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        

        return self.mergeSort(head)
