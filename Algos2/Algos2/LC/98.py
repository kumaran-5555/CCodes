# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def _isValidBST(self, node, left, right):
        if node is None:
            return True

        
        if left is not None and node.val <= left:
            return False

        if right is not None and node.val >= right:
            return False


        return self._isValidBST(node.left, left, node.val) and self._isValidBST(node.right, node.val, right)



    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        
        return self._isValidBST(root, None, None)

