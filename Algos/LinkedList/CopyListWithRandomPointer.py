#!/usr/bin/python3
__author__ = 'kumaran'

class RandomListNode():
    def __init__(self, val):
        self.label = val
        self.next = None
        self.random = None

    def __str__(self):
        node = self
        while node:
            print(("%d(")%(node.label), end="")
            if node.random:
                print("%d)->"%node.random.label, end="")
            else:
                print("None)->", end="")

            node = node.next
        return ""

class Solution():
    # @param head, a RandomListNode
    # @return a RandomListNode
    def copyRandomList(self, head):

        mapper = {}
        node = head
        while node:
            mapper[node] = RandomListNode(node.label)
            node = node.next

        retHead = None
        currNode = None
        node = head
        while node:
            if not currNode:
                currNode = mapper[node]
                retHead = currNode
            else:
                currNode.next = mapper[node]
                currNode = currNode.next

            if node.next:
                currNode.next = mapper[node.next]
            if node.random:
                currNode.random = mapper[node.random]

            node = node.next


        return retHead



if __name__ == '__main__':
    l1 = RandomListNode(1)
    l2 = RandomListNode(2)
    l3 = RandomListNode(3)
    l4 = RandomListNode(4)
    l5 = RandomListNode(5)
    l7 = RandomListNode(7)
    l1.next = l2
    l1.random = l3
    l2.next = l3
    l2.random = l5
    l3.next = l4
    l3.random = l4
    l4.next = l5
    l5.next = l7

    d = {}
    d[l1] = l2
    print(d)

    print(l1)

    s = Solution()
    new = s.copyRandomList(l1)
    print(new)

    
