class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        xor = 0

        for i in nums:
            xor ^= i

        lastbit = ((xor ^ (xor - 1)) + 1) >> 1

        a = 0
        b = 0

        for i in nums:
            if i & lastbit:
                a ^= i
            else:
                b ^= i

        return [a,b]



