#!/usr/bin/python3
__author__ = 'kumaran'


# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a boolean
    def _isSymmetric(self, t1, t2):
        if t1 and not t2:
            return False

        if t2 and not t1:
            return False

        if not t1 and not t2:
            return True

        if t1.val != t2.val:
            return False

        return self._isSymmetric(t1.left, t2.right) and self._isSymmetric(t1.right, t2.left)
    # @param root, a tree node
    # @return a boolean
    def isSymmetric(self, root):
        return  self._isSymmetric(root, root)



if __name__ == '__main__':
    s = Solution()
    
