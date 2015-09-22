#!/usr/bin/python3
__author__ = 'kumaran'

class Tree():
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None

    def printNode(cls, node):
        if not node:
            return
        if node.next:
            print(node.val, node.next.val)
        else:
            print(node.val, None)
        cls.printNode(node.left)
        cls.printNode(node.right)


class Solution():

    def setNextRightPointer(self, parent, node):
        if not parent:
            return
        print(node.val)
        if parent.left is node:
            if parent.right:
                node.next = parent.right
                return

            while parent.next:
                if parent.next.left:
                    node.next = parent.next.left
                    return
                elif parent.next.right:
                    node.next = parent.next.right
                    return
                else:
                    parent = parent.next
        else:
            while parent.next:
                if parent.next.left:
                    node.next = parent.next.left
                    return
                elif parent.next.right:
                    node.next = parent.next.right
                    return
                else:
                    parent = parent.next


        return



    # @param root, a tree node
    # @return nothing
    def connect(self, root):
        # do a moris post order traversal
        node = root
        parent = None
        while node:
            if node.right:
                temp = node.right
                while temp.left and temp.left is not node:
                    temp = temp.left

                if temp.left:
                    # seeing the node for the second time
                    parent = node
                    temp.left = None
                    node = node.left
                else:
                    # seeing the node for the first time
                    self.setNextRightPointer(parent, node)
                    temp.left = node
                    parent = node
                    node = node.right
            else:
                self.setNextRightPointer(parent, node)
                parent = node
                node = node.left
        return




if __name__ == '__main__':
    t = Tree(1)
    t.left = Tree(3)
    t.left.right = Tree(4)
    t.left.left = Tree(2)
    t.left.left.left = Tree(5)
    t.right = Tree(7)
    t.right.left = Tree(6)
    t.right.right = Tree(8)

    #Tree.printNode(Tree, t)
    s = Solution()
    s.connect(t)
    t.printNode(t)

    
