#!/usr/bin/python3
__author__ = 'kumaran'


class Trie:
    class TrieNode:
        def __init__(self):
            self.isWordBoundary = False
            self.char = None
            # links for next word
            self.links = [None] * 27

    def buildTrie(self, listOfWords):

        for w in listOfWords:
            w = w.lower()
            node = self.root
            for c in w:
                idx = ord(c)-ord('a')
                if node.links[idx] is None:
                    node.links[idx] = self.TrieNode()
                    node.links[idx].char = c

                node = node.links[idx]
            # added all chars, just mark node as word boundary
            node.isWordBoundary = True

    def _decodeTrie(self, node, str):
        if not node:
            return

        if node.isWordBoundary:
            print(str+node.char)
        for l in node.links:
            self._decodeTrie(l, str+node.char)

    def decodeTrie(self):
        for l in self.root.links:
            self._decodeTrie(l, "")

    def lookupTrie(self, word):

        '''
        :param word:
        :return: return the length of the word that is found
        '''
        node = self.root
        for c in word:
            idx = ord(c)-ord('a')
            if node.links[idx] is None:
                return False
            node = node.links[idx]
        # all chars are looked up, see if node has word boundary
        if node.isWordBoundary:
            return True

        return False

    def __init__(self):
        self.root = self.TrieNode()



class Solution():

    def __init__(self):
        self.trie = None
        self.cache = {}

    def canWordBreak(self, s, start, end):

        if start in self.cache:
            return self.cache[start]

        if start == end:
            self.cache[start] = True
            return True

        for i in range(start, end):
            if self.trie.lookupTrie(s[start:i+1]):
                # found word matching
                # see if rest of the string can be word broken
                if self.canWordBreak(s, i+1, end):
                    # done
                    self.cache[start] = True
                    return True
            else:
                pass
            # try next bigger string

        # nothing matched
        self.cache[start] = False
        return False


    # @param s, a string
    # @param dict, a set of string
    # @return a boolean
    def wordBreak(self, s, dict):
        self.cache = {}
        self.trie = Trie()
        self.trie.buildTrie(dict)
        #self.trie.decodeTrie()
        return  self.canWordBreak(s, 0, len(s))



if __name__ == '__main__':
    s = Solution()
    print(s.wordBreak("leetcode", ['leet', 'code']))
    print(s.wordBreak("samsungmehello", ['samsu', 'sam', 'sungme','hello']))
    print("")
