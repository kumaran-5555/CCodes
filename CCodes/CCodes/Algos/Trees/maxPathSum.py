#!/usr/bin/python3
__author__ = 'kumaran'

class Tree():
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None

    def printNode(cls, node):
        if not node:
            return
        if node.next:
            print(node.val, node.next.val)
        else:
            print(node.val, None)
        cls.printNode(node.left)
        cls.printNode(node.right)

class Solution():

    def __init__(self):
        self.maxPath = -999999999999

    def _maxPathSum(self, node):
        if not node:
            return 0

        # bottom-up max sum of left substree
        leftSum = self._maxPathSum(node.left)
        # bottom-up max sum of right substree
        rightSum = self._maxPathSum(node.right)

        # bottom up sum including left and rihgt substree
        crossPath = (leftSum + rightSum) + node.val

        if self.maxPath < crossPath:
            self.maxPath = crossPath

        # max path which considers, just node, or left or right substree including self
        maxPath = max(node.val, max(leftSum, rightSum) + node.val)
        if self.maxPath < maxPath:
            self.maxPath = maxPath

        return maxPath

    # @param root, a tree node
    # @return an integer
    def maxPathSum(self, root):

        self._maxPathSum(root)
        return self.maxPath



if __name__ == '__main__':

    '''
    t = Tree(1)
    t.left = Tree(2)
    t.right = Tree(3)

    t.left.right = Tree(4)
    t.left.left = Tree(2)
    t.left.left.left = Tree(5)
    t.right = Tree(7)
    t.right.left = Tree(6)
    t.right.right = Tree(8)
    '''

    t = Tree(2)
    t.left = Tree(-1)
    t.right = Tree(-2)

    t = Tree(9)
    t.left = Tree(6)
    t.right = Tree(-3)
    t.right.left = Tree(-6)
    t.right.right = Tree(2)
    t.right.right.left = Tree(2)
    t.right.right.left.left = Tree(-6)
    t.right.right.left.right = Tree(-6)

    #t = Tree(-1)
    #t.left = Tree(0)
    #t.right = Tree(1)

    s = Solution()
    print(s.maxPathSum(t))

