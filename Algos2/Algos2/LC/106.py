

class Solution_106(object):
    
    
    def _fromPostOrderAndInOrder(self, postOrderIdx, inOrderStart, inOrderEnd):
        
        if inOrderStart > inOrderEnd:
            return None

        value = self.postOrder[postOrderIdx]
        node = TreeNode(value)



        for i in range(inOrderStart, inOrderEnd+1):
            if self.inOrder[i] == value:
                break

        # size of right tree
        sizeOfRightTree = inOrderEnd - i


        node.right = self._fromPostOrderAndInOrder(postOrderIdx-1, i+1, inOrderEnd)

        node.left = self._fromPostOrderAndInOrder(postOrderIdx-1-sizeOfRightTree, inOrderStart, i-1)

        return node

        


    def buildTree(self, inOrder, postOrder):
        self.inOrder = inOrder
        self.postOrder = postOrder
        return self._fromPostOrderAndInOrder(len(postOrder)-1, 0, len(inOrder)-1)