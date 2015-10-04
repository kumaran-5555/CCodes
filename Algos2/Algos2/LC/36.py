class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        
        rowBitmaps = [0] * 9
        colBitmaps = [0] * 9
        subcellBitmaps = [0] * 9


        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    continue

                val = int(board[i][j])

                mask = 1 << val
                if rowBitmaps[i] & mask:
                    return False

                if colBitmaps[j] & mask:
                    return False

                subcellIdx = (i // 3) * 3 + (j // 3)

                if subcellBitmaps[subcellIdx] & mask:
                    return False


                rowBitmaps[i] |= mask
                colBitmaps[j] |= mask
                subcellBitmaps[subcellIdx] |= mask


        return True



                       
