# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class  Node:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):

    def maxDepth(self, node):
        count = 0

        temp = node
        while temp:
            count += 1
            temp = temp.left

        return count

    def _countNodes(self, node, depth):
        if node is None:
            return True

        leftMax = 0
        temp = node.left
        while temp:
            leftMax += 1
            temp = temp.left

        rightMax = 0
        temp = node.right

        while temp:
            rightMax += 1
            temp = temp.right

        if leftMax == rightMax and (leftMax + depth) == self.depth:
            # we have all nodes in the last level of this subtree
            self.count += (2 ** (self.depth - depth))
            return True

        if self._countNodes(node.left, depth+1):
            self._countNodes(node.right, depth+1)

        return False




        

    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
    
        self.depth = self.maxDepth(root)
        if self.depth == 0:
            return 0

        self.count = (2 ** (self.depth-1)) - 1
        
        self._countNodes(root, 1)

        return self.count



            
if __name__ == '__main__':
    s = Solution()
    t = Node(1)
    t.left = Node(2)
    t.right = Node(2)
    t.left.left = Node(3)
    t.left.right = Node(3)
    t.right.left = Node(3)
    #t.right.right = Node(3)

    #t.left.left.left = Node(4)
    #t.left.left.right = Node(4)
    #t.left.right.left = Node(4)

    s.countNodes(t)