class Solution(object):

    def _combinationSum4(self, k, n, position, prefix):
        if k == 0 and n > 0:
            return 

        if position > 9 and n > 0:
            return 



        if k == 0 and n == 0:
            self.output[tuple(prefix)] = 1
            return


        if n < position:
            return 



        for i in range(position, 10):
            o = self._combinationSum4(k-1, n-i, i+1, prefix + [i])

        

    

            


    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        self.output = {}
        self._combinationSum4(k, n, 1, [])
        return self.output.keys()

    
    
    
if __name__ == '__main__':
     s = Solution()
     s.combinationSum3(3, 10)
         