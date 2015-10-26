class SplTrie:
    def __init__(self):
        self.mapping = {}
        self.hasEnding = False



class WordDictionary(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.root = SplTrie()
        

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: void
        """
        node = self.root

        for c in word:
            if c not in node.mapping:
                node.mapping[c] = SplTrie()
            node = node.mapping[c]
        node.hasEnding = True



    def _search(self, word, pos, trie):
        if pos == len(word) and trie.hasEnding:
            return True

        elif pos == len(word):
            return False


        if word[pos] != '.' and word[pos] not in trie.mapping:
            return False

        if word[pos] != '.':
            return self._search(word, pos+1, trie.mapping[word[pos]])

        for m in trie.mapping:
            if self._search(word, pos+1, trie.mapping[m]):
                return True

        return False

        

    def search(self, word):
        """
        Returns if the word is in the data structure. A word could
        contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        rVal =  self._search(word, 0, self.root)
        return rVal



        

# Your WordDictionary object will be instantiated and called as such:
# wordDictionary = WordDictionary()
# wordDictionary.addWord("word")
# wordDictionary.search("pattern")


if __name__ == '__main__':
    w = WordDictionary()
    w.addWord('hello')
    w.addWord('helloww')
    w.addWord('kumaran')
    w.addWord('kumar')

    w.search('kumar')
    w.search('kumara')
    w.search('kumara.')
    w.search('hello')
    w.search('hel.o..')
    w.search('hel..o..')
    w.search('.....')

