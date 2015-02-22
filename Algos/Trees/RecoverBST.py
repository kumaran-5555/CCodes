#!/usr/bin/python3
__author__ = 'kumaran'


class Solution():


    def checkLocalMaximaAndMinima(self, output):
        # everytime a node added based on the current state, see if the previous
        # node forms local maxima or local minima
        if not self.isLocalMaximaFound:
            # find local maxima
            # prev.prev < prev > curr
            if len(output) < 3:
                # we don't have prev.prev
                if output[-2] > output[-1]:
                    # found local maxima
                    self.localMaxima = output[-2]
                    self.isLocalMaximaFound = True
            else:
                if output[-3] < output[-2] and output[-2] > output[-1]:
                    self.localMaxima = output[-2]
                    self.isLocalMaximaFound = True
        else:
            # find local minima, both maxima and minima can't occur at the same node
            # hence else
            # find local maxima
            # prev.prev < prev > curr
            if output[-2] > output[-1]:
                self.localMinima = output[-1]

    def inorderTraversalMoris(self, root):
        node = root
        output = []
        while node:
            if not node.left:
                # print self and go right
                output.append(node.val)
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
                output.append(node.val)
                self.checkLocalMaximaAndMinima(output)
                node = node.right
        return output


    def recoverTree(self, root):
        self.isLocalMaximaFound = False
        self.localMaxima = None
        self.localMinima = None

if __name__ == '__main__':
    s = Solution()
    
