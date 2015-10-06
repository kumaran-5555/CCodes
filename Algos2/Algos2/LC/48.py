class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)

        if n == 0:
            return

        for i in range(n):
            r = i
            c = i
            while r < n and c < n:
                temp = matrix[i][c]
                matrix[i][c] = matrix[r][i]
                matrix[r][i] = temp

                r += 1
                c += 1

        # swap cols
        for r in range(n):
            i = 0 
            j = n-1
            while i < j:
                temp = matrix[r][i]
                matrix[r][i] = matrix[r][j]
                matrix[r][j] = temp
                i += 1
                j -= 1




        return 



