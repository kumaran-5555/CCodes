class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        # firt yes position
        start = 0
        end = len(nums)-1

        if end == -1:
            return 0


        while start < end:
            mid = start + (end - start)//2

            if nums[mid] >= target:
                # go left
                end = mid
            else:
                start += 1


        if nums[end] >= target:
            return end

        else:
            return end+1

