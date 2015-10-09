class Solution(object):

    def _findKthLaregest(self, start, end):               

        
        pivot = self.nums[end]

        i = start
        j = end

        while i <= j:
            while i < end and self.nums[i] < pivot:
                i += 1

            while j >= start and self.nums[j] >= pivot:
                j -= 1

            if i > j:
                break

            temp = self.nums[i]

            self.nums[i] = self.nums[j]

            self.nums[j] = temp


        temp = self.nums[i]
        self.nums[i] = self.nums[end]
        self.nums[end] = temp

        if self.n - i == self.k:
            return self.nums[i]

        if self.n - i > self.k:
            # go right
            return self._findKthLaregest(i+1, end)

        if self.n - i < self.k:
            # go left
            return self._findKthLaregest(start, i-1)


        


    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
        self.nums = nums
        self.k = k
        self.n = len(nums)

        t =  self._findKthLaregest(0, self.n-1)
        return t



if __name__ == '__main__':
    s = Solution()
    s.findKthLargest([3,2,1,5,6,4], 5)

