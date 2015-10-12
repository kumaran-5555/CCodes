# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):

    def _hasPathSum(self, node, sum):
        if node.left is None and node.right is None and (sum - node.val) == 0:
            return True

        if node.left is None and node.right is None and (sum - node.val) != 0:
            return False

        if node.left:
            state = self._hasPathSum(node.left, sum-node.val)

            if state:
                return True

        if node.right:
            return self._hasPathSum(node.right, sum-node.val)
        
        return False

    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """

        if root is None:
            return False
        
        return self._hasPathSum(root, sum)



