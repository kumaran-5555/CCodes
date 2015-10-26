class TrieNode:
    def __init__(self):
        self.mapping = {}
        self.hasEnding = False




class Solution(object):

    def addToTrie(self, node, word):

        wl = len(word)

        i = 0
        temp = node
        while i < wl:
            if word[i] not in temp.mapping:
                temp.mapping[word[i]] = TrieNode()
        
            temp = temp.mapping[word[i]]
            i += 1
            continue
            
        temp.hasEnding = word

        

    def _findWords(self, i, j, trieNode):

        if trieNode.hasEnding:
            self.output[trieNode.hasEnding] = 1

        if i >= self.r or i < 0 or j >= self.c or j < 0 or \
            self.board[i][j] == '' or self.board[i][j] not in trieNode.mapping:
            # out-of-board, cycle, no word to continue

            return

        temp = self.board[i][j]

        self.board[i][j] = ''

        self._findWords(i+1, j, trieNode.mapping[temp])
        self._findWords(i-1, j, trieNode.mapping[temp])
        self._findWords(i, j+1, trieNode.mapping[temp])
        self._findWords(i, j-1, trieNode.mapping[temp])

        self.board[i][j] = temp




        
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        

        root = TrieNode()
        self.output = {}
        self.r = len(board)

        if self.r == 0:
            return []
        
        self.c = len(board[0])

        self.board = board



        for i in words:
            self.addToTrie(root, i)


        for i in range(self.r):
            for j in range(self.c):
                self._findWords(i, j, root)


        return self.output.keys()


if __name__ == '__main__':
    b = [
  ['o','a','a','n'],
  ['e','t','a','e'],
  ['i','h','k','r'],
  ['i','f','l','v']
]

    words = ["oath","pea","eat","rain"]
    s = Solution()
    s.findWords(b, words)


