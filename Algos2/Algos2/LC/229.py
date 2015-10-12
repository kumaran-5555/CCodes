class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        counter1 = 0
        val1 = None
        counter2 = 0
        val2 = None
        n = len(nums)


        # cancel out distinct triplets
        # after ignoring all distinct triplets, we should have n1 and n2 left without matching



        for i in range(n):

            if counter1 == 0:
                counter1 += 1
                val1 = nums[i]

            elif val1 == nums[i]:
                counter1 += 1

            elif counter2 == 0:
                counter2 += 1
                val2 = nums[i]


            elif val2 == nums[i]:
                counter2 += 1
            
            else:
                counter1 -= 1
                counter2 -= 1


        counter1 = 0
        counter2 = 0
        for i in nums:
            if i == val1:
                counter1 += 1
            elif i == val2:
                counter2 += 1

        output = []

        if counter1 > n//3:
            output.append(val1)

        if counter2 > n//3:
            output.append(val2)

        return output



if __name__ == '__main__':
    s = Solution()

    s.majorityElement([1,2,3,4,5,6,6,6,6,6,6,6,6,6,6,6,6])





