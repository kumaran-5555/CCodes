class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        


        n = len(matrix)
        if n == 0:
            return []

        m = len(matrix[0])

        output = []

        top = 0
        bottom = n-1

        left = 0
        right = m-1

        while top <= bottom and left <= right:
            # do left to right
            for i in range(left, right+1):
                output.append(matrix[top][i])

            if top ==  bottom:
                break


            # do top to bottom
            for i in range(top+1,bottom+1):
                output.append(matrix[i][right])

            if left == right:
                break


            # do right to left

            for i in range(right-1, left-1,-1):
                output.append(matrix[bottom][i])

            # do bottom to top

            for i in range(bottom-1, top, -1):
                output.append(matrix[i][left])

            top += 1
            bottom -= 1
            left += 1
            right -= 1

        return output

if __name__ == '__main__':
    s = Solution ()
    s.spiralOrder( [[2,3]])

