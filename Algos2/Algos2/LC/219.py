class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        
        nums = sorted(zip(nums, range(len(nums))))

        for i in range(len(nums)-1):
            if nums[i][0] == nums[i+1][0] and nums[i+1][1] - nums[i][1] <= k:
                return True


        return False





