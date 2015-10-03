class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        
        i = 0
        n = len(nums)
        j = n-1

        removedNums = 0

        while i <= j:
            while i < n and nums[i] != val:
                i += 1

            if i >= n or i > j:
                break

            temp = nums[i]
            nums[i] = nums[j]
            nums[j] = temp
                    
            j -= 1

        return j+1


if __name__ == '__main__':
    s = Solution()
    s.removeElement([4,5],4)


            



            





