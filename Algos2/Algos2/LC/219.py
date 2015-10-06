class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        n = len(nums)

        for i in range(n-1):
            j = 1
            while j <= k and j < n:
                if nums[i] == nums[i+j]:
                    return True

                j += 1

        return False


