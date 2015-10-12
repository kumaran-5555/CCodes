# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):

    def _rightSideView(self, node, depth):
        if node is None:
            return

        if depth not in self.output:
            self.output[depth] = node.val
            if depth > self.maxDepth:
                self.maxDepth = depth


        self._rightSideView(node.right, depth+1)
        self._rightSideView(node.left, depth+1)

        return







    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        
        self.output = {}
        self.maxDepth = -1

        self._rightSideView(root, 0)

        rVal = []

        for i in range(self.maxDepth+1):
            rVal.append(self.output[i])

        return rVal




