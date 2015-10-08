class Solution(object):

    


    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        
        n = len(matrix)

        if n == 0:
            return 0

        m = len(matrix[0])

        table = [0] * m

        maxSquare = 0

        for i in range(n):
            # update table
            for j in range(m):
                if matrix[i][j] == '1':
                    table[j] += 1
                else:
                    table[j] = 0

            # compute max

            for k in range(m):
                count = 1
                kl = k-1
                while kl >= 0 and table[kl] >= table[k]:
                    count += 1
                    kl -= 1

                kl = k+1

                while kl < m and table[kl] >= table[k]:
                    count += 1
                    kl += 1

                if count >= table[k] and table[k] > maxSquare:
                    maxSquare = table[k]


        return maxSquare ** 2


if __name__ == '__main__':
    s = Solution()
    #s.maximalSquare(['10100', '10111', '11111', '10010'])
    s.maximalSquare( ["101101","111111","011011","111010","011111","110111"])




