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
    # @param root, a tree node
    # @return nothing, do it in place
    def flatten(self, root):
        '''

        :param root:
        :return:
         modeified version of morris travel
        '''

        head = None
        tail = None
        node = root

        while node:
            # add it to the exisiting list
            if not head:
                head = node
                tail = node
            else:
                tail.right = node
                tail = node
            # if left is present, link the right most of the left to current right
            if node.left:
                temp = node.left
                while temp.right:
                    temp = temp.right

                # attach the link to come back
                temp.right = node.right

                # detach left from the current one
                temp = node.left
                node.left = None

                # go to next
                node = temp
            else:
                # go to next
                node = node.right
        return head








def printList(node):
    while node:
        print(node.val)
        node = node.right

if __name__ == '__main__':
    t = Tree(2)
    t.left = Tree(-1)
    t.right = Tree(-2)

    t = Tree(9)
    t.left = Tree(6)
    t.right = Tree(-3)
    t.right.left = Tree(-6)
    t.right.right = Tree(2)
    t.right.right.left = Tree(2)
    t.right.right.left.left = Tree(-6)
    t.right.right.left.right = Tree(-6)

    t = Tree(1)
    t.right = Tree(5)
    t.right.right = Tree(6)
    t.left = Tree(2)
    t.left.left = Tree(3)
    t.left.right = Tree(4)

    s = Solution()
    l = s.flatten(t)
    printList(l)

