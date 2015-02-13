__author__ = 'kumaran'

class Solution:
    # @param matrix, a list of lists of integers
    # @return a list of integers
    def spiralOrder(self, matrix):
        rows = len(matrix)
        cols = 0
        if not rows:
            return []

        if rows:
            cols =  len(matrix[0])

        output = []
        mStartRow = 0
        mEndRow = rows-1
        mStartCol = 0
        mEndCol = cols-1
        case = "LR"
        i=0
        j=0
        while mStartCol <= mEndCol and mStartRow <= mEndRow:

            if case == "LR":
                while j <= mEndCol:
                    output.append(matrix[i][j])
                    j += 1
                j -= 1
                case = "TD"
                mStartRow += 1
                i += 1
            elif case == "TD":
                while i <= mEndRow:
                    output.append(matrix[i][j])
                    i += 1
                i -= 1
                case = "RL"
                mEndCol -= 1
                j -= 1

            elif case == "RL":
                while j >= mStartCol:
                    output.append(matrix[i][j])
                    j -= 1
                j += 1
                case = "DT"
                mEndRow -= 1
                i -= 1
            elif case == "DT":
                while i >= mStartRow:
                    output.append(matrix[i][j])
                    i -= 1
                i += 1
                case = "LR"
                mStartCol += 1
                j += 1


        return output
x


