# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):

    def lca(self, node, p, q):

        if node is None:
            return None

        if node.val < p.val and node.val < q.val:
            # go right
            return self.lca(node.right, p, q)

        elif node.val > p.val and node.val > q.val:
            # go left
            return self.lca(node.left, p, q)

        return node



    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if root is None:
            return None

        return self.lca(root, p, q)

