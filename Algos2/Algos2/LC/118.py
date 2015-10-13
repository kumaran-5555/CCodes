class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        
        prev = [[1]]

        n = numRows

        for i in range(1,rowIndex):
            temp = [1]
            for j in range(i-1):
                temp.append(prev[i-1][j] + prev[i-1][j+1])

            temp.append(1)

            prev = temp

        return prev

