# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):

    def _lowestCommonAncestor(self, node, state):
        if node is None:
            return

        if state[self.lca] is not None:
            return 
        
        if state[self.left] and state[self.right]:
            return


        canBeLca = state[self.lca] is None and state[self.left] is False and state[self.right] is False

        if node is self.p:
            state[self.left] = True


        if node is self.q:
            state[self.right] = True

        


        self._lowestCommonAncestor(node.left, state)
        self._lowestCommonAncestor(node.right, state)

        if canBeLca and state[self.lca] is None and state[self.left] and state[self.right]:
            state[self.lca] = node
            return

        

    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        self.p = p
        self.q = q
        self.left = 0
        self.right = 1
        self.lca = 2

        state = [False, False, None]


        self._lowestCommonAncestor(root, state)

        return state[self.lca]












if __name__ == '__main__':
    
    t = TreeNode(37)
    t.left = TreeNode(-34)
    t.left.right = TreeNode(-100)
    t.right = TreeNode(-48)
    x = TreeNode(-100)
    t.right.left = x
    t.right.right = TreeNode(48)
    t.right.right.left = TreeNode(-54)
    y = TreeNode(-71)
    t.right.right.left.left = y
    t.right.right.left.right = TreeNode(-22)
    t.right.right.left.right.right = TreeNode(8)


    s = Solution()
    s.lowestCommonAncestor(t,x, y)



