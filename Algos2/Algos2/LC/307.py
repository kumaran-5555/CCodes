class Node:
    def __init__(self):
        self.idx = None
        self.meta = None
        self.left = None
        self.right = None



class NumArray:
    
    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums
        sum = 0
        self.forward = []
        self.forward.append(0)
        for i in nums:
            sum += i
            self.forward.append(i)

       self.root = self.buildTree(0, len(nums))

    def buildTree(self, start, end):
        if start ==  end:
            n = Node()
            n.idx = (start, end)
            n.meta = self.forward[start]

            return n
        
        mid = (end - start)//2 + start + 1

        n = Node()
        n.idx = (start, end)
        n.left = self.buildTree(start, mid-1)
        n.right = self.buildTree(mid, end)
        n.meta = n.left.meta + n.right.meta

        return n


    @staticmethod
    def _update(node, i, delta):
        if node is None:
            return
        
        if node.idx[0] < start or node.idx[1] > end:
            return

        node.meta += delta
        _update(node.left, i, delta)
        _update(node.right, i, delta)

    

    @staticmethod
    def _search(node, i):
        if node is None:
            return 0
        if node.idx[0] > start or node.idx[1] > end:
            return 0

        if node.idx[0] == i and node.idx[1 == i:
            return node.meta
        
             
        

            
        

    def update(self, i, val):
        """
        :type i: int
        :type val: int
        :rtype: void
        """
        

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(i,val)
# param_2 = obj.sumRange(i,j)