class Solution(object):
    def _solveSudoku(self, row, col):
        #print(self.board, row, col)

        if row >= 81:
            return True

        r = row // 9
        c = col % 9

        
        if self.board[r][c] != '.':
            if self._solveSudoku(row+1, col+1):
                return True
            return False


        # try numbers
        for i in range(1,10):
            mask = 1 << i

            if self.rowBitmap[r] & mask:
                continue

            if self.colBitmap[c] & mask:
                continue

            if self.cellBitmap[(r//3) * 3 + c//3] & mask:
                continue

            self.rowBitmap[r] |= mask
            self.colBitmap[c] |= mask
            self.cellBitmap[(r//3) * 3 + c//3] |= mask


            self.board[r][c] = str(i)

            if self._solveSudoku(row+1, col+1):
                return True

            self.board[r][c] = '.'

            self.rowBitmap[r] &= ~mask
            self.colBitmap[c] &= ~mask
            self.cellBitmap[(r//3) * 3 + c//3] &= ~mask

        return False


    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        self.rowBitmap = [0] * 9
        self.colBitmap = [0] * 9
        self.cellBitmap = [0] * 9

        self.board = []

        for r in range(9):
            for c in range(9):
                if c == 0:
                    self.board.append([0]*9)

                self.board[r][c] = board[r][c]

                if board[r][c] == '.':
                    continue

                mask = 1 << int(board[r][c])

                self.rowBitmap[r] |= mask
                self.colBitmap[c] |= mask
                self.cellBitmap[(r//3) * 3 + c//3] |= mask

        self._solveSudoku(0,0)
        for r in range(9):
            board[r] = ''.join(self.board[r])

        return 





if __name__ == '__main__':
    s = Solution()
    s.solveSudoku(["..9748...","7........",".2.1.9...","..7...24.",".64.1.59.",".98...3..","...8.3.2.","........6","...2759.."])