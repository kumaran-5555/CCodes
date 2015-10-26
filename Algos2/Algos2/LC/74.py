class Solution(object):

    def binSearchRows(self):
        
        start = 0
        end = self.r-1

        while start < end:
            mid = start + (end - start)//2

            # greater than or euqal
            if self.matrix[mid][0] < self.target:
                start = mid  + 1

            else:
                end = mid

        if self.matrix[end][0] >= self.target:
            return end

        return -1

    def binSearchCol(self, row):

        start = 0
        end = self.c-1

        while start <= end:
            mid = start + (end - start)//2

            if row[mid] < self.target:
                start = mid + 1

            elif row[mid] > self.target:
                end = mid - 1

            else:
                return True


        return False




    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        

        self.r = len(matrix)

        if self.r == 0:
            return False

        self.c = len(matrix[0])

        self.matrix = matrix
        self.target = target


        row = self.binSearchRows()
        if row == -1:
            return self.binSearchCol(self.matrix[self.r-1])

        if self.matrix[row][0] == target:
            return True

        if row == 0:
            return False

        return self.binSearchCol(self.matrix[row-1])

if __name__ == '__main__':
    s = Solution()
    s.searchMatrix([  [1]], 1)

