class NumMatrix(object):

    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        self.sum = matrix
        self.r = len(matrix)
        if self.r == 0:
            self.sum = None
            return
        self.c = len(matrix[0])
        for i in range(self.r):
            for j in range(self.c):                                    
                sum = self.sum[i][j]
                if i > 0:
                    sum += self.sum[i-1][j]
                if j > 0:
                    sum +=  self.sum[i][j-1]
                if i > 0 and j > 0:
                    sum -=  self.sum[i-1][j-1]

                self.sum[i][j] = sum


        pass


        

    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        if self.sum == None:
            return 0

        sum = self.sum[row2][col2]
        row1 -= 1
        col1 -=1 

        if row1 >= 0 and col1 >= 0:
            sum -= self.sum[row1][col1]
            sum -= (self.sum[row1][col2] - self.sum[row1][col1])
            sum -= (self.sum[row2][col1] - self.sum[row1][col1])
        elif row1 >= 0:
            sum -= self.sum[row1][col2]

        elif col1 >= 0:
            sum -= self.sum[row2][col1]


        return sum




# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)

if __name__ == '__main__':
    c =  NumMatrix( [
  [3, 0, 1, 4, 2],
  [5, 6, 3, 2, 1],
  [1, 2, 0, 1, 5],
  [4, 1, 0, 1, 7],
  [1, 0, 3, 0, 5]
])

    c.sumRegion(2,1,4,3)
