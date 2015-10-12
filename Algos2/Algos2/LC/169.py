class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        # cancel out distinct pairs, we should have number left out for which we didn't find any match
        # check whether that is max

        counter = 0
        val = None

        for i in nums:
            if counter == 0:
                counter += 1
                val = i

            elif val == i:
                counter += 1

            else:
                counter -= 1


        return val


