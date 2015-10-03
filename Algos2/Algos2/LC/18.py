
from collections import defaultdict

class Solution(object):

    def twoSums(self, nums, start, end, target, first, second):

        
        i = start
        j = end

        while i < j:
            sum = nums[i] + nums[j]

            if sum == target:
                self.result[(first, second, nums[i], nums[j])] = 1
                while i < end and nums[i+1] == nums[i]:
                    i += 1

                i += 1

                while j > start and nums[j-1] == nums[j]:
                    j -= 1
                j -= 1
            elif sum < target:
                i += 1

            else:
                j -= 1

        return None

    def threeSum(self, nums, start, end, target, first):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        for i in range(start, end):
            if i > start and nums[i] == nums[i-1]:
                continue
            self.twoSums(nums, i+1, end, target-nums[i], first, nums[i])



    def fourSum2(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        self.result = {}
        
        nums = sorted(nums)
        n = len(nums)

        for i in range(n-3):
            if i > 0 and nums[i] == nums[i-1]:
                continue

            for j in range(i+1, n):
                if j > i+1 and nums[j] == nums[j-1]:
                    continue
                self.twoSums(nums, j+1, n-1, target-nums[i]-nums[j], nums[i], nums[j])

        return self.result.keys()


    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        self.result = {}

        nums = sorted(nums)
        n = len(nums)

        self.twoSumDict = defaultdict(dict)

        for i in range(n):
            for j in range(i+1, n):
                self.twoSumDict[nums[i]+num[j]][(i, j)] = 1

        for s in self.twoSumDict:
            if target-s in self.twoSumDict:
                for t1 in self.twoSumDict[s]:
                    for t2 in self.twoSumDict[target-s]:
                        if t1[0] not in t2 and t1[1] not in t2:
                            self.result[(sorted(nums[t1[0]], nums[t1[1]], nums[t2[0]], nums[t2[1]]))] = 1

        return self.result.keys()




            

