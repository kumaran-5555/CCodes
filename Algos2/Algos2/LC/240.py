class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        rowMin = 0
        rowMax = len(matrix)-1

        colMin = 0
        if rowMax >= 0:
            colMax = len(matrix[0])-1
        else:
            return False


        while rowMin <= rowMax and colMin <= colMax:
            # compare top right
            if target > matrix[rowMin][colMax]:
                # ignore top row
                rowMin += 1

            elif target < matrix[rowMin][colMax]:
                # ignore last col
                colMax -= 1

            else:
                return True

            # compare bottom left
            if target > matrix[rowMax][colMin]:
                # ignore firs col
                colMin += 1

            elif target < matrix[rowMax][colMin]:
                # ignore last row
                rowMax -= 1

            else:
                return True


        return False


