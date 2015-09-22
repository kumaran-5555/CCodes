#!/usr/bin/python3
__author__ = 'kumaran'


# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:

    def inorderTraversalMoris(self, root):
        node = root
        output = []
        while node:
            if not node.left:
                # print self and go right
                output.append(node.val)
                node = node.right
                continue

            temp = node.left

            while temp.right and temp.right is not node:
                temp = temp.right

            if not temp.right:
                # we are aboubt to enter the left subtree for the
                # first time, create a way to comeback
                temp.right = node
                node = node.left
            else:
                # we just came back from the left subtree we
                # entered earlier, reset the tree
                temp.right = None
                output.append(node.val)
                node = node.right
        return output

    def inorderTraversalStack(self, root):
        output = []
        stack = []

        if not root:
            return []
        stack.append([root, "BeforeLeft"])

        while len(stack):
            curr = stack[-1]

            currState = curr[1]
            currNode = curr[0]

            if not currNode:
                stack.pop()
                continue

            if currState == "BeforeLeft":
                curr[1] = "AfterLeft"
                stack.append([currNode.left, "BeforeLeft"])
            elif currState == "AfterLeft":
                output.append(currNode.val)
                curr[1] = "AfterRight"
                stack.append([currNode.right, "BeforeLeft"])
            elif currState == "AfterRight":
                stack.pop()

        return output


    # @param root, a tree node
    # @return a list of integers
    def inorderTraversal(self, root):
        return self.inorderTraversalMoris(root)

















if __name__ == '__main__':
    s = Solution()

