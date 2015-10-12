class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        
        output = []

        n = len(nums)
        if n == 0:
            return output

        start = nums[0]
        prev = nums[0]

        for i in range(1, n):
            if nums[i] == prev + 1:
                prev += 1

            else:
                # sequence is broken
                if prev == start:
                    output.append(str(start))

                else:
                    output.append('{0}->{1}'.format(start, prev))
                
                prev = nums[i]
                start = nums[i]


        # sequence is broken
        if prev == start:
            output.append(str(start))

        else:
            output.append('{0}->{1}'.format(start, prev))


        return output




