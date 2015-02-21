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




if __name__ == '__main__':
    t = Trie()
    t.buildTrie(["A", "to", "tea", "ted", "ten", "i", "in", "inn"])
    t.decodeTrie()
    print(t)
