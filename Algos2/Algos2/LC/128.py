class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """


        n = len(nums)

        d = {}
        seen = {}

        maxLength = 0

        for i in range(n):
            if nums[i] in seen:
                continue

            seen[nums[i]] = 1
            left = nums[i] - 1
            right = nums[i] + 1

            

            if left in d and d[left][1] <= left and right in d and d[right][0] >= right:
                # merge
                nLeft = d[left][0]
                nRight = d[right][1]

                del d[d[left][1]]
                del d[d[right][0]]

                d[nLeft] = [nLeft, nRight]
                d[nRight] = [nLeft, nRight]

                if maxLength < nRight - nLeft + 1:
                    maxLength = nRight - nLeft + 1

            elif left in d and d[left][1] <= left:
                # increase

                nLeft = d[left][0]

                del d[d[left][1]]

                d[nLeft] = [nLeft, nums[i]]
                d[nums[i]] = [nLeft, nums[i]]

                if maxLength < nums[i] - nLeft + 1:
                    maxLength = nums[i] - nLeft + 1

            elif right in d and d[right][0] >= right:
                # increase
            
                nRight = d[right][1]

                del d[d[right][0]]

                d[nRight] = [nums[i], nRight]
                d[nums[i]] = [nums[i], nRight]

                if maxLength < nRight - nums[i] + 1:
                    maxLength = nRight - nums[i] + 1

            else:
                # new number
                d[nums[i]] = [nums[i], nums[i]]

                if maxLength < 1:
                    maxLength = 1


        return maxLength






if __name__ == '__main__':
    s = Solution()
    s.longestConsecutive([100, 4, 200, 1, 3, 2])





                 


