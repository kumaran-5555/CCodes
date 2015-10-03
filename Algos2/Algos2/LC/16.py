class Solution(object):
    def twoSums(self, nums, start, end, target):
        i = start
        j = end
        bestDiff = float('inf')
        v1 = None
        v2 = None

        while i < j:
            sum = nums[i] + nums[j]
            if abs(target - sum) < bestDiff:
                bestDiff = abs(target - sum)
                v1 = nums[i]
                v2 = nums[j]



            if sum == target:
                break
            elif sum < target:
                i += 1
            else:
                j -= 1


        # this should difinite yeidl solution, if there are at least two numbers
        return v1 + v2
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums = sorted(nums)
        bestDiff = float('inf')

        answer = None

        n = len(nums)
        for i in range(n-2):
            output = self.twoSums(nums, i+1, n-1, target-nums[i])
            diff = abs(target - (output + nums[i]))
            if  diff < bestDiff:
                bestDiff = diff
                answer = output + nums[i]




            
        return answer


if __name__ == '__main__':
    s = Solution()
    s.threeSumClosest([1,1,1,0], -100)
