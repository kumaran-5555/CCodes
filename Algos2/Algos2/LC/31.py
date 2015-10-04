class Solution(object):

    def reverseRange(self, list, start, end):
        while start < end:
            temp = list[start]
            list[start] = list[end]
            list[end] = temp

            start += 1
            end += 1


    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        
        i = 0
        k = -1
        n = len(nums)
        for i in range(n-1):
            if nums[i] < nums[i+1]:
                k = i

        if k == -1:
            # next one doesn't exists
            self.reverseRange(nums, 0, n-1)
            return


        
        j = k+2
        l = k+1

        while j < n:
            if nums[k] < nums[j]:
                l = j
                j += 1

            else:
                break

        # swap j and k
        temp = nums[k]
        nums[k] = nums[l]
        nums[l] = temp

        self.reverseRange(nums, k+1, n-1)

        return 


if __name__ == '__main__':
    s = Solution()
    t = s.nextPermutation( [1,3,2])
    print(t)



            