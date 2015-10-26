class Solution(object):
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        
        n = len(ratings)

    
        temp = [1] * n

        for i in range(1,n):
            if ratings[i-1] < ratings[i]:
                temp[i] = (temp[i-1] + 1)

        for i in range(n-2,-1,-1):
            if ratings[i] > ratings[i+1]:
                temp[i] = max(temp[i], temp[i+1] + 1)


        return sum(temp)




if __name__ == '__main__':
    s = Solution()
    s.candy([1,2,2,3])
