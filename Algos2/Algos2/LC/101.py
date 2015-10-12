# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def _isSymetric(self, n1, n2):

        if n1 is None and n2 is None:
            return True

        if n1 is None or n2 is None:
            return False

        if n1.val != n2.val:
            return False

        return self._isSymetric(n1.left, n2.right) and self._isSymetric(n1.right, n2.left)


    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        
        return self._isSymetric(root, root)


