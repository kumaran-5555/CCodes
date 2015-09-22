#!/usr/bin/python3
__author__ = 'kumaran'
# https://oj.leetcode.com/problems/lru-cache/

class LRUCache:

    class DoublyLinkedList:
        def __init__(self, val, key):
            self.val = val
            self.key = key
            self.prev = None
            self.next = None

    # @param capacity, an integer
    def __init__(self, capacity):
        self.size = 0
        self.capacity = capacity
        self.list = None
        self.listHead = None
        self.listTail = None
        # stores key to DoublyLinkedList node
        self.keys = {}

    def printCache(self):
        node = self.listHead
        while node:
            print("%d -> %d, "%(node.key, node.val), end="")
            node = node.next
        print()

    # @return an integer
    def get(self, key):
        if key in self.keys:
            self.updateKeyReference(key, self.keys[key].val)
            #print(self.keys[key].val)
            return self.keys[key].val
        else:
            #print(-1)
            return -1

    def addKeyWithCapacity(self, key, value):
        # cache has empty slots when this is called
        # cache is not full yet
        self.size += 1
        node = self.DoublyLinkedList(value, key)
        self.keys[key] = node
        if self.listTail:
            # list the node to tail
            self.listTail.next = node
            node.prev = self.listTail

        if not self.listHead:
            # if not head, mark the current as head
            self.listHead = node

        # change the tail
        self.listTail = node

    def delLeastUsedFromCache(self):
        # cache is full
        # remove the head
        node = self.listHead
        # move the head to point to next node
        self.listHead = self.listHead.next

        # if new head is present, reset it is prev
        if self.listHead:
            self.listHead.prev = None

        # if capacity is 1, tail is also removed
        if self.capacity == 1:
            self.listTail = None

        # remove the node from dict
        self.keys.pop(node.key, None)

        # remove the node itself
        del node

        self.size -= 1

    def updateKeyReference(self, key, value):
        # key exists in the cache, just update its reference
        node = self.keys[key]

        prev = node.prev
        next = node.next
        if prev:
            prev.next = next
        else:
            # current node is at the head
            self.listHead = next

        if next:
            next.prev = prev
        else:
            # current node is at the tail
            self.listTail = prev

        # delete the node and add it as new with
        self.keys.pop(key, None)
        del node
        self.size -= 1

        self.addKeyWithCapacity(key, value)


    # @param key, an integer
    # @param value, an integer
    # @return nothing
    def set(self, key, value):
        if key not in self.keys:
            # new key
            if self.size < self.capacity:
                self.addKeyWithCapacity(key, value)

            else:
                self.delLeastUsedFromCache()
                self.addKeyWithCapacity(key,value)
        else:
            self.updateKeyReference(key, value)











if __name__ == '__main__':
    s = LRUCache(2)

    s.set(2,1)
    s.printCache()
    s.set(1,1)
    s.printCache()
    s.get(2)
    s.printCache()
    s.set(4,1)
    s.printCache()
    s.get(1)
    s.printCache()
    s.get(2)
    s.printCache()


