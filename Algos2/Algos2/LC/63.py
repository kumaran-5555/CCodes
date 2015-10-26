class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        
        grid = []

        r = len(obstacleGrid)
        if r == 0:
            return 0

        c = len(obstacleGrid[0])

        for i in range(r):
            for j in range(c):
                if j == 0:
                    grid.append([0]*c)

                if i == 0 and j == 0 and obstacleGrid[i][j] == 0:
                    grid[i][j] = 1
                    continue

                if obstacleGrid[i][j] == 1:
                    continue

                top, left = 0 ,0

                if i > 0 and obstacleGrid[i-1][j] != 1:
                    top = grid[i-1][j]

                if j > 0 and obstacleGrid[i][j-1] != 1:
                    left = grid[i][j-1]

                grid[i][j] = top + left



        return grid[r-1][c-1]






