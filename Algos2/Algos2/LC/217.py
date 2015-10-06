class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) == 0:
            return False

        mem = {}
        for n in nums:
            if n in mem:
                return True

            mem[n] = 1


        return False
