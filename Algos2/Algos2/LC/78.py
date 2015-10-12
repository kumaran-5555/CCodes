class Solution(object):

    def _subsets(self, i, prefix):

        if i >= self.n:
            self.output.append(prefix)

        # use this number
        self._subsets(i+1, prefix + [self.nums[i]])

        # ignore this numbers

        self._subsets(i+1, prefix)


    def _subsets2(self):

        for i in range(1, (2 ** self.n)-1):
            temp = []
            for j in range(0,self.n):
                if (1 << j) & i:
                    temp.append(self.nums[j])

            self.output.append(temp)






    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        self.output = []
        self.nums = nums
        self.n = len(nums)

        self._subsets2()



        return self.output



