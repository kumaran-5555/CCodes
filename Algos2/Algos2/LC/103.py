
from collections import deque

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        


        output = []

        queue = deque()
        
        count = 0

        if root is None:
            return output

        queue.append(root)
        queue.append('#')


        temp = []
        while len(queue):
            
            node = queue.popleft()

            if node == '#':
                if count % 2 == 0:
                    output.append(temp)
                else:
                    temp.reverse()
                    output.append(temp)
                    
                temp = []

                count += 1

                if len(queue):
                    queue.append('#')
                continue
            temp.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)


        return output


        