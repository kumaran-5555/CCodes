# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):

    def _isSameTree(self, p, q):

        if not p and not q:
            return True


        if (p is None and q) or (q is None and p) or (p and q and p.val != q.val):
            return False
        
        return self._isSameTree(p.left, q.left) and self._isSameTree(p.right, q.right)


        


    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        
        return self._isSameTree(p, q)


