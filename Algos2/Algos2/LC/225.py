from collections import deque


class Stack(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.lastElement = None
        self.activeQueue = deque()
        self.inactiveQueue = deque()
                                 

        

    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        self.activeQueue.append(x)

                

    def pop(self):
        """
        :rtype: nothing
        """
        n = len(self.activeQueue)

        while n > 1:
            self.inactiveQueue.append(self.activeQueue.popleft())
            n -= 1

        rVal = self.activeQueue.popleft()

        temp = self.activeQueue
        self.activeQueue = self.inactiveQueue
        self.inactiveQueue = temp

        return rVal




        


    def top(self):
        """
        :rtype: int
        """
        n = len(self.activeQueue)

        while n > 1:
            self.inactiveQueue.append(self.activeQueue.popleft())
            n -= 1

        rVal = self.activeQueue.popleft()

        self.inactiveQueue.append(rVal)

        temp = self.activeQueue
        self.activeQueue = self.inactiveQueue
        self.inactiveQueue = temp

        return rVal



    def empty(self):
        """
        :rtype: bool
        """
        
        return len(self.activeQueue) == 0
