class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        
        grid = []

        if m == 0 or n == 0:
            return 0


        for i in range(m):
            for j in range(n):
                if j == 0:
                    grid.append([0] * n)
                if i == 0 and j == 0:
                    grid[i][j] = 1
                    continue
                top, left = 0, 0
                if m > 0:
                    top = grid[i-1][j]
                    
                if j > 0:
                    left = grid[i][j-1]

                grid[i][j] = top + left


        return grid[m-1][n-1]






