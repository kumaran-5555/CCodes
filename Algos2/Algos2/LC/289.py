class Solution(object):

    def state(self, i, j):
        totalLive = 0
        currLive = self.board[i][j] == 1 or self.board[i][j] == 2


        if i > 0:
            # top is present
            if j > 0 and self.board[i-1][j-1]:
                # left top
                totalLive += 1

            if j < self.c-1 and self.board[i-1][j+1]:
                # right top
                totalLive += 1
            
            if self.board[i-1][j]:
                # top
                totalLive += 1

        if j > 0 and self.board[i][j-1]:
            # left is presnt
            totalLive += 1

        if j < self.c-1 and self.board[i][j+1]:
            # right is prsent
            totalLive += 1

        if i < self.r-1:
            # bottom is present
            if j > 0 and self.board[i+1][j-1]:
                # left bottom 
                totalLive += 1

            if j < self.c-1 and self.board[i+1][j+1]:
                # right bottom
                totalLive += 1
            if self.board[i+1][j]:
                # bottom
                totalLive += 1

        if currLive and totalLive < 2:
                return 2
        elif (totalLive == 2 or totalLive == 3) and currLive:
            return 1

        elif currLive and totalLive > 3:
            return 2

        elif not currLive and totalLive == 3:
            return None
        
        return self.board[i][j]

    
    
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        # 2 - dead after update
        # None - newly live after update
        
        self.board = board
        self.r = len(board)
        if self.r:
            self.c = len(board[0])


        for i in range(self.r):
            for j in range(self.c):
                self.board[i][j] = self.state(i, j)

        # replace 2s to 0
        # replace Nones to 1
        for i in range(self.r):
            for j in range(self.c):
                if self.board[i][j] == 2:
                    self.board[i][j] = 0
                elif self.board[i][j] is None:
                    self.board[i][j] = 1

        return


if __name__ == '__main__':
     s = Solution()
     board = [[0, 0, 0, 0, 0],
             [0, 1, 1, 1, 0],
             [0, 0, 0, 0, 0,]]
     
     s.gameOfLife(board)
                