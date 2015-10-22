# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        prevPrev = None
        prev = None

        dupCount = 0

        curr = head

        newHead = None

        while curr:
            if prev and curr.val == prev.val:
                # duplicate
                dupCount += 1

            elif prev:
                if dupCount == 0:
                    # not duplicate, prev is not duplicate
                    if newHead is None:
                        newHead = prev

                    prevPrev = prev
                    prev = curr
                else:
                    dupCount = 0
                    if prevPrev:
                        # prev is duplicate, cut short the prev
                        prevPrev.next = curr
                    else:
                        pass

                    prev = curr

            else:
                prev = curr

            curr = curr.next
            
            
        if dupCount > 0:
            # tail has duplicate, if possible cut it out
            if prevPrev:
                prevPrev.next = None
                
        else:

            # not duplicate, prev is not duplicate
            if newHead is None:
                newHead = prev
            
                
                


        return newHead


