from collections import deque


# Definition for binary tree with next pointer.
# class TreeLinkNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution(object):
    def connect(self, root):
        """
        :type root: TreeLinkNode
        :rtype: nothing
        """
        

        q = deque()

        if root is None:
            return 

        q.append(None)
        q.append(root)
        

        prev = None
        while len(q):

            node = q.popleft()

            if node is None:
                prev = None
                if len(q):
                    q.append(None)
                continue

            node.next = prev

            if node.right:
                q.append(node.right)

            if node.left:
                q.append(node.left)

            prev = node


            






