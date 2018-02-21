class Node:
    def __init__(self):
        self.idx = None
        self.meta = None
        self.left = None
        self.right = None
        self.mid =  None



class NumArray:
    
    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.n = nums                
        if len(nums) == 0:
            return
        self.root = self.buildTree(0, len(nums)-1)

    def buildTree(self, start, end):
        if start ==  end:
            n = Node()
            n.idx = (start, end)
            n.meta = self.n[start]
            n.mid = start

            return n
        
        mid = (end - start)//2 + start + 1

        n = Node()
        n.idx = (start, end)
        n.left = self.buildTree(start, mid-1)
        n.right = self.buildTree(mid, end)
        n.meta = n.left.meta + n.right.meta
        n.mid = mid

        return n


    @staticmethod
    def _update(node, i, delta):
        if node is None:
            return
        
        if node.idx[0] > i or node.idx[1] < i:
            return

        node.meta += delta
        NumArray._update(node.left, i, delta)
        NumArray._update(node.right, i, delta)

    

    @staticmethod
    def _search(node, i, j):
        if i > j:
            return 0
        if node is None:
            return 0
        
        if node.idx[0] >= i and node.idx[1] <= j:            
            return node.meta

        if node.idx[0] > i and node.idx[0] > j:
            return 0

        if node.idx[1] < i and node.idx[1] < j:
            return 0

        return NumArray._search(node.left, i, j) + NumArray._search(node.right, i, j)

        
    def update(self, i, val):
        """
        :type i: int
        :type val: int
        :rtype: void
        """
        
        delta = val - self.n[i]
        
        NumArray._update(self.root, i, delta)
        self.n[i] = val



    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        
        return NumArray._search(self.root, i, j)



# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(i,val)
# param_2 = obj.sumRange(i,j)

if __name__ == '__main__':
    
    c = NumArray([7,2,7,2,0])
    print(c.update(4, 6))
    print(c.sumRange(0,2))
    print(c.update(1, 2))
    print(c.sumRange(0,2))