#!/usr/bin/python3
__author__ = 'kumaran'

import copy

class Solution:
    def __init__(self):
        self.count = 0

    def isValidMove(self, board, row, col, size):
        # check only rows above this

        # check for col intersect
        for i in range(0, row):
            if board[i][col] == 'Q':
                return False


        # check diagonal to top right
        j = row - 1
        for i in range(col + 1, size):
            if j < 0:
                break
            if board[j][i] == 'Q':
                return False
            j -= 1

        # check diagonal to top left
        j = row - 1
        for i in range(col - 1, -1, -1):
            if j < 0:
                break
            if board[j][i] == 'Q':
                return False

            j -= 1

        return True


    def queenProblem(self, board, currRow, size):
        if currRow == size:
            self.count += 1
            temp = []
            for i in board:
                temp.append("".join(i))
            self.output.append(temp[:])
            return

        for i in range(0, size):
            if self.isValidMove(board, currRow, i, size):
                board[currRow][i] = 'Q'
                self.queenProblem(board, currRow + 1, size)
                board[currRow][i] = '.'

    # @return an integer
    def solveNQueens(self, n):
        self.output = []
        board = []
        size = n
        for i in range(size):
            board.append(['.'] * size)
        self.queenProblem(board, 0, size)
        return self.output


if __name__ == '__main__':
    s = Solution()
    print(s.solveNQueens(4))
    
