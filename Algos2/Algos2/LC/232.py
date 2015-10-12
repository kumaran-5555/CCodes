from collections import deque


class Queue(object):

    def invertActiveInactive(self):

        n = len(self.activeStack)
        while n > 0:
            self.inactiveStack.append(self.activeStack.pop())

        self.inverted = not self.inverted


    def __init__(self):
        """
        initialize your data structure here.
        """
        self.activeStack = []
        self.inactiveStack = []
        self.inverted = False
        

    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        if self.inverted:
            self.invertActiveInactive()

        self.activeStack.append(x)



        

    def pop(self):
        """
        :rtype: nothing
        """
        
        if not self.inverted:
            self.invertActiveInactive()

        rVal = self.activeStack.pop()
        return rVal

             

    def peek(self):
        """
        :rtype: int
        """

        if not self.inverted:
            self.invertActiveInactive()

        return self.activeStack[-1]

        

    def empty(self):
        """
        :rtype: bool
        """
        return len(self.activeStack) == 0