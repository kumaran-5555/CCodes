# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):

    def _maxDepth(self, node, depth):
        if node is None:
            return depth

        return max(self._maxDepth(node.left, depth+1), self._maxDepth(node.right, depth+1))

    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
    
        return self._maxDepth(root, 0)
