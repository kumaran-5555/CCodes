# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):

    def _sumNumbers(self, node, subTotal):

        if node.left is None and node.right is None:
            self.total += (subTotal * 10 + node.val)
            return



        if node.left:
            self._sumNumbers(node.left, subTotal * 10 + node.val)

        if node.right:
            self._sumNumbers(node.right, subTotal * 10 + node.val)




    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        self.total = 0

        self._sumNumbers(root, 0)

        return total

