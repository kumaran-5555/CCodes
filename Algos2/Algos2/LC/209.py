class Solution(object):

    def predicate(self, start, end, s):

        return self.leftToRight[end] - self.leftToRight[start] + self.nums[start] >= s




    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        
        n = len(nums)
        self.nums = nums

        # binary search the answer

        # cumulative sum from left ot right
        self.leftToRight = []
        total = 0
        for i in nums:
            if i >= s:
                return 1
            total += i
            self.leftToRight.append(total)


        minLength = n+1

        start = 0
        end = n-1

        while start < end:
            length = start + (end - start) // 2

            i = 0

            while i+length < n:
                if self.predicate(i, i+length, s):
                    # we can try smaller
                    if minLength > length+1:
                        minLength = length+1
                    end = length
                    break
                i+=1


            if end != length:
                # not found enough
                # try increasing the length
                start = length + 1


        if minLength ==  n+1:
            return 0

        return minLength


            


            

if __name__ == '__main__':
    s = Solution()
    s.minSubArrayLen(7, [2,3,1,2,4,3])



