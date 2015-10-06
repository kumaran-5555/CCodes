class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        mem = {}
        for n in nums:
            if n in mem:
                return False

            mem[n] = 1


        return True
