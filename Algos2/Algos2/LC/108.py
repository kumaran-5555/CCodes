# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def _buildTree(self, nums, start, end):

        if start > end:
            return None

        rootIdx = start + (end - start) // 2

        root = TreeNode(nums[rootIdx])

        root.left = self._buildTree(nums, start, rootIdx-1)
        root.right = self._buildTree(nums, rootIdx+1, end)


        return root


    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        
        return self._buildTree(nums, 0, len(nums)-1)

