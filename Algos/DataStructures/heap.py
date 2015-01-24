__author__ = 'serajago'

import copy
import ctypes

class Heap():
    def __init__(self, a):
        self.array = copy.deepcopy(a)
        self.length = len(a)

    def maxHeapify(self, i):
        left = 2 * i + 1
        right = 2 * i + 2
        largest = i

        # see if left child is bigger than the parent
        if left < self.length and self.array[left] > self.array[i]:
            largest = left
        # see right child is bigger than the parent
        if right < self.length and self.array[right] > self.array[largest]:
            largest = right

        if largest != i:
            temp = self.array[i]
            self.array[i] = self.array[largest]
            self.array[largest] = temp
            # start heapifying the modified child
            self.maxHeapify(largest)

    def buildHeap(self):
        # last leaf's parent self.length-1/2
        # do bottom up
        for i in range(int((self.length - 1) / 2), -1, -1):
            self.maxHeapify(i)
            print(self.array)

    def removeRoot(self):
        # del it root, add last element as root and heapify
        temp = self.array[0]
        self.array[0] = self.array[self.length - 1]
        self.length -= 1
        self.maxHeapify(0)
        return temp


    def __str__(self):
        return str(self.array[:self.length])

l = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
h = Heap(l)
h.buildHeap()
print(h.removeRoot())
print(Heap.maxHeapify)

print(id(l))
print(id(h.array))
print(h)
l[0] = 100
print(h)