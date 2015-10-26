class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        
        r = len(grid)

        if r == 0:
            return 0

        c = len(grid[0])

        for i in range(r):
            for j in range(c):
                top, left = 0, 0

                if i > 0 and j > 0:
                    grid[i][j] += min(grid[i-1][j], grid[i][j-1])
                    
                elif i > 0:
                    grid[i][j] += grid[i-1][j]
                    
                elif j > 0:
                    grid[i][j] += grid[i][j-1]
                    


        return grid[r-1][c-1]

