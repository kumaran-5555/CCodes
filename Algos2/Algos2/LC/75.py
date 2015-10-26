class Solution(object):
    def sortColors2(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        
        n = len(nums)
        nonZero = 0

        zero = n-1

        while nonZero <= zero:
            while nonZero < n and nums[nonZero] == 0:
                nonZero += 1

            while zero >= 0 and nums[zero] != 0:
                zero -= 1

            if nonZero > zero:
                break


            temp =  nums[zero]
            nums[zero] = nums[nonZero]
            nums[nonZero] = temp

            nonZero += 1
            zero -= 1

        # nonZero points first 1 or 2

        one = nonZero
        two = n-1

        while one < two:
            while one < n-1 and nums[one] == 1:
                one += 1

            while two >= nonZero and nums[two] == 2:
                two -= 1

            if one >= two:
                break


            temp = nums[one]
            nums[one] = nums[two]
            nums[two] = temp

            one += 1
            two -= 1

        return
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """

        n = len(nums)

        cursor = 0
        left = 0
        right = n-1

        while cursor <= right:
            if nums[cursor] < 1:
                temp = nums[left]
                nums[left] = nums[cursor]
                nums[cursor] = temp
                cursor += 1
                left += 1
                
            elif nums[cursor] > 1:
                temp = nums[right]
                nums[right] = nums[cursor]
                nums[cursor] = temp
                
                right -= 1
                
            else:
                cursor += 1
                
        return
                     






if __name__ == '__main__':
    s = Solution()

    s.sortColors([1,0,0])





