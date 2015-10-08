class Solution(object):
    def productExceptSelf2(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        n = len(nums)
        output = []

        if n == 0:
            return output
        
        # output[i] = product of nums[1] ... nums[i]
        product = 1
        
        for i in range(n):
            product *= nums[i]
            output.append(product)
            
        # product at while processing i - keeps products of nums[i+1] ... nums[n-1]

        # output[i] = output[i-1] * product

        product = 1
        for i in range(n-1, 0, -1):
            output[i] = output[i-1] * product
            product *=  nums[i]

        output[0] = product



        return output


