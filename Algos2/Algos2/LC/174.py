class Solution(object):
    def calculateMinimumHP(self, dungeon):
        """
        :type dungeon: List[List[int]]
        :rtype: int
        """
        
        r = len(dungeon)

        if r == 0:
            return 0

        c = len(dungeon[0])

        # we update each cell to minimum health
        # required at the previous stage to reach 
        # princess through i,j

        for i in range(r-1, -1, -1):
            for j in range(c-1, -1, -1):

                if i == r-1 and j == c-1:
                    if dungeon[i][j] > 0:
                        dungeon[i][j] = 0

                    else:
                        dungeon[i][j] = -dungeon[i][j]

                else:

                    if j < c-1 and i < r-1:
                        bottom = dungeon[i+1][j]
                        right = dungeon[i][j+1]

                        if dungeon[i][j] > min(bottom, right):
                            dungeon[i][j] = 0
                        else:
                            dungeon[i][j] = -dungeon[i][j] + min(bottom, right)

                    elif j < c-1:
                        right = dungeon[i][j+1]
                        if dungeon[i][j] > right:
                            dungeon[i][j] = 0
                        else:
                            dungeon[i][j] = -dungeon[i][j] + right

                    elif i < r-1:
                        bottom = dungeon[i+1][j]

                        if dungeon[i][j] > bottom:
                            dungeon[i][j] = 0
                        else:
                            dungeon[i][j] = -dungeon[i][j] + bottom


        return dungeon[0][0] + 1









                   