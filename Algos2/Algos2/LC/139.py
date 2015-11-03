class Trie:
    def __init__(self):
        self.mapping = {}

        self.hasEnd = None


    def add(self, word, root):

        temp = root
        i = 0
        while i < len(word):
            if word[i] not in temp.mapping:
                temp.mapping[word[i]] = Trie()

            temp = temp.mapping[word[i]]

            i += 1

        temp.hasEnd = word


    def searchPrefix(self, word, root, lengthConstraint):
        '''
            minimum length of the prefix to match
            return length of the prefix found
        '''

        i = 0

        temp = root

        while i < len(word):

            if temp.hasEnd != None and i >= lengthConstraint:
                # found prefix with lengthConstraing
                return i

            if word[i] not in temp.mapping:
                # can't proceed
                return 0
        

            
            temp = temp.mapping[word[i]]

            i += 1

        if temp.hasEnd != None:
            return i



        return 0


class Solution(object):

    def _wordBreak(self, pos):
        if pos == self.n:
            
            return True

        if pos in self.dp:
            return self.dp[pos]
        
        for i in range(pos, self.n):
            matchLen = self.root.searchPrefix(self.s[pos:], self.root, i-pos+1)

            if matchLen == 0:
                # we can't find any prefix longer than this,
                break

            if self._wordBreak(pos+matchLen):
                return True

        self.dp[pos] = False
        return False

    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: Set[str]
        :rtype: bool
        """
        
        self.dp = {}

        self.s = s
        self.n = len(s)

        self.root = Trie()

        for w in wordDict:
            self.root.add(w, self.root)

        rVal = self._wordBreak(0)
        return rVal





if __name__ == '__main__':
    s = Solution()
    s.wordBreak('leetcod', ['leet' , 'cod' , 'e'])

    


