# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def _pathSum(self, node, sum, path):

        if node.left is None and node.right is None and node.val == sum:
            self.output.append(path + [node.val])
            return

        if node.left:
            self._pathSum(node.left, sum-node.val, path + [node.val])

        if node.right:
            self._pathSum(node.right, sum-node.val, path + [node.val])

        return



    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        
        self.output = []

        if root is None:
            return self.output

        self._pathSum(root, sum, [])

        return self.output

