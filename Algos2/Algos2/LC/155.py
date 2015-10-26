class MinStack(object):
    def __init__(self):
        """
        initialize your data structure here.

        """

        self.numStack = []
        self.minStack = []
        self.n = 0
        

    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """

        if self.n > 0:
            if self.minStack[-1] >= x:
                self.minStack.append(x)
        else:
            self.minStack.append(x)

        self.numStack.append(x)

    def pop(self):
        """
        :rtype: nothing
        """
        
        if self.minStack[-1] == self.numStack[-1]:
            self.minStack.pop()

        
        self.numStack.pop()

    def top(self):
        """
        :rtype: int
        """
        

        return self.numStack[-1]

    def getMin(self):
        """
        :rtype: int
        """
    
        return self.minStack[-1]    