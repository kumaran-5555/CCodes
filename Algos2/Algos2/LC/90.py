class Solution(object):


    def _subsets2(self):

        for i in range(1, (2 ** self.n)-1):
            temp = []
            for j in range(0,self.n):
                if (1 << j) & i:
                    temp.append(self.nums[j])

            self.output[tuple(temp)] = 1






    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        self.output = {}
        self.nums = nums
        self.n = len(nums)

        self._subsets2()



        return self.output.keys()



