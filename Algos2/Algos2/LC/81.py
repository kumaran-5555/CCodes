class Solution(object):


    def recursiveRotatedBinarySearch(self, left, right):


        nums = self.nums

        target = self.target


        if left > right:
            return False

        mid = left + (right - left)//2

        if nums[mid] == target:
            return True

        # if length <= 10
        # do linear search
        if right - left <= 10:
            for i in range(left, right+1):
                if nums[i] == target:
                    return True
            return False


        if nums[mid] < nums[left] and nums[mid] < nums[right]:
            # left side is rotated

            if nums[mid] < target and target <= nums[right]:
                # go right
                ret = self.recursiveRotatedBinarySearch(mid+1, right)

            else:
                # go left
                ret = self.recursiveRotatedBinarySearch(left, mid-1)

#

        elif nums[mid] > nums[left] and nums[mid] > nums[right]:
            # right side is rotated part
            if nums[mid] > target and target >= nums[left]:
                # go left
                ret = self.recursiveRotatedBinarySearch(left, mid-1)

            else:
                # go right
                ret = self.recursiveRotatedBinarySearch(mid+1, right)


        else:

            # we should search both on left and right
            ret = self.recursiveRotatedBinarySearch(left, mid-1)

            if ret == False:
                ret = self.recursiveRotatedBinarySearch(mid+1, right)


        return ret









        
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        self.nums = nums
        self.target = target

        
        return self.recursiveRotatedBinarySearch(0, len(nums)-1)
