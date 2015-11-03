# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        
        '''
        mooris
        '''

        output = []
        node = root

        while node:

            if node.left:
                temp = node.left

                while temp.right and temp.right != node:
                    temp = temp.right

                if temp.right is None:
                    # create a back link
                    temp.right = node
                    # go to left tree
                    node = node.left

                else:
                    # we just finished left branch
                    # reset the back link
                    temp.right = None
                    output.append(node.val)
                    node = node.right

            else:
                output.append(node.val)
                node = node.right

        return output


