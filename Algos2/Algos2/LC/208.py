class TrieNode(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """

        self.edges = {}

        self.hasEnding = False

        

class Trie(object):

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        
        temp = self.root
        for c in word:
            if c in temp.edges:
                temp = temp.edges[c]
                continue

            temp.edges[c] = TrieNode()

            temp = temp.edges[c]

        # set ending flag

        temp.hasEnding = True

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        
        temp = self.root
        for c in word:
            if c not in temp.edges:
                return False

            temp = temp.edges[c]

        if temp.hasEnding:
            return True

        return False


    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie
        that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        
        temp = self.root
        for c in prefix:
            if c not in temp.edges:
                return False

            temp = temp.edges[c]

        return True


# Your Trie object will be instantiated and called as such:
# trie = Trie()
# trie.insert("somestring")
# trie.search("key")