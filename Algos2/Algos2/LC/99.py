# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Node:
    def __init__(self, x):
        self.val = x
        self.left = None

        self.right = None

class Solution(object):
    def _recoverTree(self, node, prev):
        if node is None:
            return prev

        

        prev = self._recoverTree(node.left, prev)

        if prev and node.val < prev.val and len(self.broken) == 0:
            self.broken.append(prev)
            self.broken.append(node)

        elif prev and node.val < prev.val and len(self.broken) == 2:
            self.broken[1] = node

        return self._recoverTree(node.right, node)




    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        
        self.broken = []

        self._recoverTree(root, None)

        if len(self.broken):
            self.broken[0].val, self.broken[1].val = self.broken[1].val, self.broken[0].val

        return


if __name__ == '__main__':
    s = Solution()
    t = Node(0)
    t.left = Node(1)
    s.recoverTree(t)