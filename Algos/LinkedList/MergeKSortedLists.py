#!/usr/bin/python3
__author__ = 'kumaran'

import heapq
class Node():
    def __init__(self, val):
        self.val = val
        self.next = None

class Solution():

    def nextSmall(self, lists, heap):

        minHeapNode = heapq.heappop(heap)
        if not minHeapNode:
            return None
        idx = minHeapNode[1]
        minNode = lists[idx]

        # update the lists
        lists[idx] = minNode.next

        # update the heap
        if lists[idx]:
            heapq.heappush(heapq, (lists[idx].val, idx))

        return minNode

    def initializeHeap(self, lists, size):
        heap = []
        for i in range(size):
            if lists[i]:
                heapq.heappush(heap, (lists[i].val, i))

        return heap

    # @param a list of ListNode
    # @return a ListNode
    def mergeKLists(self, lists):
        head = None
        tail = None
        k = len(lists)
        heap = self.initializeHeap(lists, k)
        while True:
            node = self.nextSmall(lists, heap)
            if not node:
                break
            if not head:
                head = node
            if tail:
                tail.next = node

            tail = node

        return head


if __name__ == '__main__':
    s = Solution()
    
