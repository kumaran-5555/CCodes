#!/usr/bin/python3
__author__ = 'kumaran'

import time

class Solution():
    def __init__(self):
        self.board = None

    def isValidMove(self, row, col):

        if self.board[row][col] == '.':
            return True
        # check row
        bitmap = {}
        for i in range(9):
            if self.board[row][i] == '.':
                continue

            if self.board[row][i] in bitmap:
                return False
            else:
                bitmap[self.board[row][i]] = 1

        # check column
        bitmap = {}
        for i in range(9):
            if self.board[i][col] == '.':
                continue

            if self.board[i][col] in bitmap:
                return False
            else:
                bitmap[self.board[i][col]] = 1

        # check current box
        bitmap = {}
        boxRow = (row // 3) * 3
        boxCol = (col // 3) * 3
        for i in range(boxRow, boxRow+3):
            for j in range(boxCol, boxCol+3):
                if self.board[i][j] == '.':
                    continue
                if self.board[i][j] in bitmap:
                    return False
                else:
                    bitmap[self.board[i][j]] = 1

        return True

    # @param board, a 9x9 2D array
    # @return a boolean
    def isValidSudoku(self):
        for i in range(9):
            for j in range(9):
                if not self.isValidMove(i, j):
                    return False
        return True

    # @param board, a 9x9 2D array
    # @return a boolean
    def _solveSudoku(self, position):
        row = position // 9
        col = position % 9
        if position == 81:
            self.isSolved = True
            self.solution = []
            for i in range(9):
                self.solution.append(''.join([ str(j) for j in self.board[i]]))
            return

        if self.board[row][col] != '.':
            # it is already ensured that what we have is correct
            self._solveSudoku(position+1)
            return
        for v in range(1,10):
            self.board[row][col] = v
            if not self.isValidMove(row, col):
                continue
            self._solveSudoku(position+1)
            if self.isSolved:
                # don't change anything
                return

        self.board[row][col] = '.'




    # @param board, a 9x9 2D array
    # Solve the Sudoku by modifying the input board in-place.
    # Do not return any value.
    def solveSudoku(self, board):
        self.board = []
        self.solution = None
        self.isSolved = False
        for i in range(9):
            self.board.append(['.'] * 9)

        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    self.board[i][j] = int(board[i][j])
        self._solveSudoku(0)
        for i in range(9):
            board[i] = self.solution[i]
        #print(board)
        #[print(i) for i in board]




if __name__ == '__main__':
    s = Solution()
    start = time.time()
    #print(s.solveSudoku([".....7..9",".4..812..","...9...1.","..53...72","293....5.",".....53..","8...23...","7...5..4.","531.7...."]))
    b = ["..9748...","7........",".2.1.9...","..7...24.",".64.1.59.",".98...3..","...8.3.2.","........6","...2759.."]
    print(s.solveSudoku(b))
    print(b)
    print(time.time()-start)


