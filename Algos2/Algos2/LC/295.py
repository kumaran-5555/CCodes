import heapq





class MedianFinder:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.minHeap = []
        self.maxHeap = []

        self.minHeapSize = 0
        self.maxHeapSize = 0



    def addNum(self, num):
        """
        Adds a num into the data structure.
        :type num: int
        :rtype: void
        """
        
        if self.minHeapSize == self.maxHeapSize:
            if self.minHeapSize > 0 and num >= self.minHeap[0]:
                heapq.heappush(self.minHeap, num)
                self.minHeapSize += 1
            else:
                heapq.heappush(self.maxHeap, -num)
                self.maxHeapSize += 1

        else:
            if self.minHeapSize > self.maxHeapSize:
                if num >= self.minHeap[0]:
                    # we need to balance
                    v = heapq.heappop(self.minHeap)
                    heapq.heappush(self.maxHeap, -v)

                    heapq.heappush(self.minHeap, num)

                    self.maxHeapSize += 1
                else:
                    heapq.heappush(self.maxHeap, -num)
                    self.maxHeapSize += 1

            else:
                if num < -1 * self.maxHeap[0]:

                    # we need to balance
                    v = heapq.heappop(self.maxHeap) * -1
                    heapq.heappush(self.minHeap, v)

                    heapq.heappush(self.maxHeap, -num)

                    self.minHeapSize += 1
                    
                else:
                    heapq.heappush(self.minHeap, num)
                    self.minHeapSize += 1

        return

    def findMedian(self):
        """
        Returns the median of current data stream
        :rtype: float
        """
        

        if self.minHeapSize == self.maxHeapSize:
            return (self.minHeap[0] - self.maxHeap[0]) / 2.0
        elif self.minHeapSize > self.maxHeapSize:
            return float(self.minHeap[0])
        else:
            return -1 * self.maxHeap[0]



# Your MedianFinder object will be instantiated and called as such:
# mf = MedianFinder()
# mf.addNum(1)
# mf.findMedian()

if __name__ == '__main__':
    s = MedianFinder()

    for i in [6, 10,2,6,5,0,6,3,1,0,0]:
        s.addNum(i)
        print(s.findMedian())
