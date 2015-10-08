# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):

    def _binaryTreePaths(self, node, path):
        if node.left is None and node.right is None:
            self.output.append("->".join(path))
            return 

        if node.left:
            self._binaryTreePaths(node.left, path+[str(node.val)])

        if node.righ:
            self._binaryTreePaths(node.right, path+[str(node.val)])


       
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        self.output = []

        if root is None:
            return []

        self._binaryTreePaths(root, [])

        return self.output

