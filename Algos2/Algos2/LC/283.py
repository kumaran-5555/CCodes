class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        
        # i - tracks zeros
        # j - tracks non-zeros

        n = len(nums)

        i = 0
        j = 0
        prev = 0 
        while i < n:
            while i < n and nums[i] != 0:
                i += 1

            if i == n:            
                return

            while j < n and nums[j] == 0:
                j += 1

            if j == n:
                return

            if j < i:
                j += 1
                continue


            temp = nums[i]
            nums[i] = nums[j]
            nums[j] = temp

            i += 1


if __name__ == '__main__':
    s = Solution()
    s.moveZeroes([0,1,0,3,12])
