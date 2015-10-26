# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):

    def _flatten(self, node):
        if node.left is None and node.right is None:
            return (node, node)

        temp = node.right
        
        tailL = None
        headL = None
        
        headR = None
        tailR = None

        if node.left:
            headL, tailL = self._flatten(node.left)

        if temp:
            headR, tailR = self._flatten(temp)

        # connect and return

        if headL:
            node.right = headL
            node.left = None
            tailL.right = headR
        else:
            node.right = headR


        if headR:
            return (node, tailR)
        else:
            return (node, tailL)




    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        if root is None:
            return
        
        self._flatten(root)[0]

