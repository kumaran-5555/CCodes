class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        
        n = len(triangle)

        if n == 0:
            return 0

        temp1 = [0] * n
        temp = [0] * n

        temp[0]  = triangle[0][0]

        for i in range(1,n):
            for j in range(i+1):
                if j > 0 and j < i:
                    temp1[j] = min(temp[j-1] + triangle[i][j] , temp[j] + triangle[i][j])

                elif j > 0:
                    temp1[j] = temp[j-1] + triangle[i][j]

                elif j < i:
                    temp1[j] = temp[j] + triangle[i][j]
                

            temp2 = temp
            temp = temp1
            temp1 = temp2


        return min(temp)


if __name__ == '__main__':
    s = Solution()
    s.minimumTotal([
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
])


    

                

