class Solution(object):
    def expandIsland(self, i, j):
        if i >= self.r or j >= self.c or i < 0 or j < 0:
            return 

        if self.grid[i][j] == '0' or self.grid[i][j] == '2':
            return

        self.grid[i][j] = '2'

        self.expandIsland(i+1, j)
        self.expandIsland(i-1, j)
        self.expandIsland(i, j+1)
        self.expandIsland(i, j-1)



    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        self.grid = []

        self.r = len(grid)
        if self.r == 0:
            return 0

        for i in range(self.r):
            self.grid.append(list(grid[i]))



        self.c = len(grid[0])
        total = 0
        for i in range(self.r):
            for j in range(self.c):
                if self.grid[i][j] == '1':
                    total += 1
                    self.expandIsland(i, j)


        return total



if __name__ == '__main__':
    s = Solution()
    s.numIslands(['11000', '11000', '00100', '00011'])



