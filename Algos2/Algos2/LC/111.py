# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def _minDepth(self, node, depth):
        if node.left is None and node.right is None:
            if depth < self.output:
                self.output = depth
            return

        if node.left:
            self._minDepth(node.left, depth+1)
        if node.right:
            self._minDepth(node.right, depth+1)



    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.output = float('inf')
        
        if root is None:
            return 0
            
            

        self._minDepth(root, 1)
        
        return self.output

