class Solution(object):

    def checkWord(self, i, j, pos):
        
        if self.hasFound:
            return
        
        if pos == self.n and not self.hasFound:
            self.hasFound = True
            return

        if i < 0 or j < 0 or i >= self.r or j >= self.c or pos >= self.n:
            return



        if self.board[i][j] != self.word[pos]:
            return


        temp = self.board[i][j]

        # flagging
        self.board[i][j] = ''

        self.checkWord(i+1, j, pos+1)
        self.checkWord(i-1, j, pos+1)
        self.checkWord(i, j+1, pos+1)
        self.checkWord(i, j-1, pos+1)

        self.board[i][j] = temp







    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        
        self.r = len(board)

        if self.r == 0:
            return False

        self.c = len(board[0])

        self.n = len(word)

        self.board = board
        self.word = word

        self.hasFound = False

        for i in range(self.r):
            for j in range(self.c):
                self.checkWord(i, j, 0)

                if self.hasFound:
                    return True


        return False




