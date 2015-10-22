from collections import deque

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        
        if root is None:
            return []

        q = deque()

        q.append(root)
        q.append('#')

        output = []
        temp = []
        while len(q):
            node = q.popleft()
            if node == '#' and len(q):
                output.append(temp)
                temp = []
                q.append('#')
            elif node == '#':
                output.append(temp)

            else:
                temp.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

        return output

            