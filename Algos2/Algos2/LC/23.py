
import heapq

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        
        head = None
        tail = None

        heap = heapq()


        # initialize heap
        n = len(lists)
        for i in range(n):
            if lists[i]:
                heapq.heappush(heap, (lists[i].val, lists[i]))


        while len(heap):
            val, node = heapq.heappop(heap)

            if tail is None:
                tail = node
                head = node

            else:
                tail.next = node
                tail = node

            node = node.next

            if node:
                heapq.heappush(heap, node.val, node)

        if tail:
            tail.next = None


        return head



