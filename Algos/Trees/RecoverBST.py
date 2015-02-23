#!/usr/bin/python3
__author__ = 'kumaran'

class Tree():
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Solution():


    def checkLocalMaximaAndMinima(self, output):
        if len(output) < 2:
            return
        # everytime a node added based on the current state, see if the previous
        # node forms local maxima or local minima
        if not self.isLocalMaximaFound:
            # find local maxima
            # prev > curr
            if output[-2].val > output[-1].val:
                # found local maxima
                self.localMaxima = output[-2]
                self.isLocalMaximaFound = True
        # find local maxima
        # prev.prev < prev > curr
        if output[-2].val > output[-1].val:
            self.localMinima = output[-1]

    def inorderTraversalMoris(self, root):
        node = root
        output = []
        while node:
            if not node.left:
                # print self and go right
                output.append(node)
                self.checkLocalMaximaAndMinima(output)
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
                output.append(node)
                self.checkLocalMaximaAndMinima(output)
                node = node.right
        return output


    def recoverTree(self, root):
        self.isLocalMaximaFound = False
        self.localMaxima = None
        self.localMinima = None
        self.inorderTraversalMoris(root)
        #print(self.localMaxima, self.localMinima)
        if not self.localMaxima or not self.localMinima:
            return

        temp = self.localMaxima.val
        self.localMaxima.val = self.localMinima.val
        self.localMinima.val = temp
        return root
        '''
        self.localMaxima = None
        self.localMinima = None
        self.inorderTraversalMoris(root)
        print(self.localMaxima, self.localMinima)
        '''

if __name__ == '__main__':
    t = Tree(1)
    t.left = Tree(3)
    t.left.right = Tree(4)
    t.left.left = Tree(2)
    t.left.left.left = Tree(5)
    t.right = Tree(7)
    t.right.left = Tree(6)
    t.right.right = Tree(8)

    t = Tree(0)
    t.left = Tree(1)
    s = Solution()
    s.recoverTree(t)


