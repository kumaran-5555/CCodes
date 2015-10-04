class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None



    @staticmethod
    def _inorderTraversal(node):
        if node is None:
            return

        BinaryTree._inorderTraversal(node.left)
        print('{} '.format(node.value))
        BinaryTree._inorderTraversal(node.right)



    def inorderTraversal(self):
        BinaryTree._inorderTraversal(self.root)



    @staticmethod
    def _preorderTraversal(node):
        if node is None:
            return

        BinaryTree._preorderTraversal(node.left)
        BinaryTree._preorderTraversal(node.right)
        print('{} '.format(node.value))

    def preorderTraversal(node):
        BinaryTree._preorderTraversal(self.root)


    @staticmethod
    def _postorderTraversal(node):
        if node is None:
            return

        print('{} '.format(node.value))
        BinaryTree._postorderTraversal(node.left)
        BinaryTree._postorderTraversal(node.right)

    def postorderTraversal(self):
        BinaryTree._postorderTraversal(self.root)



    def inorderTraversalMoris(self):

        node = self.root


        while node:

            if node.left:


                temp = node.left

                while temp.right and temp.right != node:
                    temp = temp.right

                if temp.right is None:
                    # create link
                    temp.right = node                    
                    node = node.left

                else:
                    # break link
                    temp.right = None

                    print('{} '.format(node.value))

                    node = node.right

            else:
                print('{} '.format(node.value))
                node = node.right
    
    @staticmethod
    def _fromPostOrderAndInOrder(postOrderIdx, inOrderStart, inOrderEnd):

        value = self.inOrder[postOrderIdx]
        node = Node(value)

        if inOrderEnd == inOrderStart:            
            return node
                

        for i in range(inOrderStart, inOrderEnd+1):
            if self.postOrder[i] == value:
                break

        # size of right tree
        sizeOfRightTree = inOrderEnd - i

        if i != inOrderEnd:
            # right is prsent
            node.right = BinaryTree._fromPostOrderAndInOrder(postOrderIdx-1, i+1, inOrderEnd)

        if i != inOrderStart:
            # left is present
            node.left = BinaryTree._fromPostOrderAndInOrder(postOrderIdx-1-sizeOfRightTree, inOrderStart, i-1)

        return node

        


    def fromPostOrderAndInOrder(self, inOrder, postOrder):
        self.inOrder = inOrder
        self.postOrder = postOrder
        BinaryTree._fromPostOrderAndInOrder(len(postOrder)-1, 0, len(inOrder)-1)



    




class Helpers(object):
    def inOrderSuccessor(self,node):
    
        if node.right is None:
            return None

        temp = node.right



        while temp.left and temp.left != node:
            temp = temp.left

        return temp


    def inOrderPredecessor(self, node):
        if node.left is None:
            return None

        temp = node.left

        while temp.right and temp.right != node:
            temp = temp.right

        return temp










        
        



if __name__ == '__main__':
    s = Solution_105()
    t1 = s.buildTree( [4,2,1,3,6,5,7], [1,2,3,4,5,6,7])



    print(t)



    

