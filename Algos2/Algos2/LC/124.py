# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Tree:
    def __init__(self, x):
        self.val =  x 
        self.left = None
        self.right = None


class Solution(object):

    def _maxPathSum(self, node):
        if node.left is None and node.right is None:
            if self.maxSum < node.val:
                self.maxSum = node.val
            return node.val

        leftSum = 0
        rightSum = 0
        if node.left:
            leftSum = self._maxPathSum(node.left)

        if node.right:
            rightSum = self._maxPathSum(node.right)


        if self.maxSum < max(leftSum + node.val, rightSum + node.val, node.val, leftSum + node.val + rightSum):
            self.maxSum = max(leftSum + node.val, rightSum + node.val, node.val, leftSum + node.val + rightSum)

        return max(node.val, node.val + leftSum, rightSum + node.val)

        

    def _maxPathSumTopDown(self, node, sum):
        if node is None:
            return sum


        leftSum = self._maxPathSumTopDown(node.left, sum+node.val)
        rightSum = self._maxPathSumTopDown(node.right, sum+node.val)


        if self.maxSum < max(sum+node.val, leftSum - sum, rightSum - sum, leftSum, rightSum, leftSum + rightSum - (2*sum) - node.val):
            self.maxSum = max(sum+node.val, leftSum - sum, rightSum - sum, leftSum, rightSum, leftSum + rightSum - (2*sum) - node.val)


        return max(sum+node.val, leftSum, rightSum)





    

    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        if root is None:
            return 0


        self.maxSum = float('-inf')

        self._maxPathSumTopDown(root, 0)

        return self.maxSum


if __name__ == '__main__':
    s = Solution()
    t = Tree(-1)
    t.left = Tree(0)
    t.right = Tree(1)

    s.maxPathSum(t)