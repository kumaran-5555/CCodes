#!/usr/bin/python3
__author__ = 'kumaran'


class Solution():
    def __init__(self):
        self.board = None

    def isValidMove(self, row, col):

        if self.board[row][col] == '.':
            return True
        # check row
        bitmap = 0
        for i in range(9):
            if self.board[row][i] == '.':
                continue

            if bitmap & (1 << int(self.board[row][i])):
                return False
            else:
                bitmap |= (1 << int(self.board[row][i]))

        # check column
        bitmap = 0
        for i in range(9):
            if self.board[i][col] == '.':
                continue

            if bitmap & (1 << int(self.board[i][col])):
                return False
            else:
                bitmap |= (1 << int(self.board[i][col]))

        # check current box
        bitmap = 0
        boxRow = (row // 3) * 3
        boxCol = (col // 3) * 3
        for i in range(boxRow, boxRow+3):
            for j in range(boxCol, boxCol+3):
                if self.board[i][j] == '.':
                    continue
                if bitmap & (1 << int(self.board[i][j])):
                    return False
                else:
                    bitmap |= (1 << int(self.board[i][j]))

        return True



    # @param board, a 9x9 2D array
    # @return a boolean
    def isValidSudoku(self, board):
        self.board = board
        for i in range(9):
            for j in range(9):
                if not self.isValidMove(i, j):
                    return False


        return True



if __name__ == '__main__':
    s = Solution()
    print(s.isValidSudoku([[4,8,3,9,2,1,6,5,7],
[9,6,7,3,4,5,8,2,1],
[2,5,1,8,7,6,4,9,3],
[5,4,8,1,3,2,9,7,6],
[7,2,9,5,6,4,1,3,8],
[1,3,6,7,9,8,2,4,5],
[3,7,2,6,8,9,5,1,4],
[8,1,4,2,5,3,7,6,9],
[6,9,5,4,1,7,3,8,'.']]))

    
