# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):

    def _kthSmallest(self, node):
        if node is None:
            return

        if self.count >= self.k:
            return


        self._kthSmallest(node.left)
        self.count += 1

        if self.count == self.k:
            self.rval = node.val
            return

        self._kthSmallest(node.right)





    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        self.k = k
        self.count = 0
        self.rval = None

        self._kthSmallest(root)


        return self.rval