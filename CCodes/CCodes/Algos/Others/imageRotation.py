#!/usr/bin/python3
__author__ = 'kumaran'


class Solution():
    # @param matrix, a list of lists of integers
    # @return a list of lists of integers
    def rotate(self, matrix):
        # swap rows and cols
        # then do reverse of cols
        i = 0
        l = len(matrix)
        if not l:
            return  []

        while i < l:
            # swap i th row with i th col
            for j  in range(i, l):
                temp = matrix[i][j]
                matrix[i][j] = matrix[j][i]
                matrix[j][i] = temp
            i += 1

        # reverse cols
        i = 0
        j = l-1
        while i < j:
            # swap values
            for k in range(l):
                temp = matrix[k][i]
                matrix[k][i] = matrix[k][j]
                matrix[k][j] = temp
            i += 1
            j -= 1
        return  matrix


if __name__ == '__main__':
    s = Solution()
    s.rotate([[1,2,3],[4,5,6],[7,8,9]])

