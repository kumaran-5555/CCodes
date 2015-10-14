# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Tree:
    def __init__ (self, x):
        self.val = x 
        self.left = None
        self.right = None



# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):

    def _isBalanced(self, node, depth):
        if node is None:
            return depth


        lMax = self._isBalanced(node.left, depth+1)

        rMax = self._isBalanced(node.right, depth+1)

        if (abs(lMax - rMax) > 1) and self.balanced:
            self.balanced = False

        
        return max(lMax, rMax)



    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        
        # we take min, max depth from both left and right child
        # compare min, max of alternate sides and see the diff

        self.balanced = True

        self._isBalanced(root, 0)

        return self.balanced







if __name__ == '__main__':
    s = Solution()
    t = Tree(1)
    t.left = Tree(2)
    t.right = Tree(2)

    t.left.left = Tree(3)
    t.left.right = Tree(3)
    t.right.left = Tree(3)
    t.right.right = Tree(3)

    t.left.left.left = Tree(4)
    t.left.left.right = Tree(4)
    t.left.right.left = Tree(4)
    t.left.right.right = Tree(4)
    t.right.left.left = Tree(4)
    t.right.left.right = Tree(4)
    
    t.left.left.left.left = Tree(5)
    t.left.left.left.right = Tree(5)

    s.isBalanced(t)

