class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        nums = zip(nums, range(len(nums)))
        nums = sorted(nums, key=lambda x: x[0])
        
        n = len(nums)
        i = 0
        j = n-1

        while i < j:
            sum = nums[i][0] + nums[j][0]
            if  sum == target:
                return sorted([nums[i][1]+1, nums[j][1]+1])
            elif sum > target:
                # we need less to get sum
                j -= 1
            else:
                # we need more to get sum
                i += 1



if __name__ == '__main__':
    s = Solution()
    print(s.twoSum([3,2,4], 6))
