
class Solution_105(object):
        
    def _fromPostOrderAndInOrder(self, preOrderIdx, inOrderStart, inOrderEnd):
        
        if inOrderStart > inOrderEnd:
            return None

        value = self.preOrder[preOrderIdx]
        node = TreeNode(value)


        i = self.inOrderPositions[value]
         

        # size of right tree
        sizeOfLeftTree =  i - inOrderStart
        
        node.right = self._fromPostOrderAndInOrder(preOrderIdx+1+sizeOfLeftTree, i+1, inOrderEnd)

        node.left = self._fromPostOrderAndInOrder(preOrderIdx+1, inOrderStart, i-1)

        return node

        


    def buildTree(self, preOrder, inOrder):
        self.inOrder = inOrder
        self.preOrder = preOrder

        # inorder positions
        self.inOrderPositions = {}
        for i in range(len(self.inOrder)):
            self.inOrderPositions[self.inOrder[i]] = i
        return self._fromPostOrderAndInOrder(0, 0, len(inOrder)-1)

