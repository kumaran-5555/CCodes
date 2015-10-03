class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        i = 0
        j = 0
        prev = None
        n = len(nums)
        if n < 2:
            return n

        prev = nums[0]
        j = 1 
        i = 1
        while j < n:
            while j < n and nums[j] == prev:
                j += 1

                
            if j >= n:
                break

                
            prev = nums[j]
            temp = nums[j]
            nums[j] = nums[i]
            nums[i] = temp

            j += 1
            i += 1

        return i


                

        