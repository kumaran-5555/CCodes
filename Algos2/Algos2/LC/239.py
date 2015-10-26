from collections import deque

class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        
        window = deque()
        
        n = len(nums)

        output = []

        for i in range(n):

            while len(window) and window[-1][0] <= nums[i]:
                window.pop()
            window.append((nums[i],i))


            while len(window) and window[0][1] <= i-k:
                window.popleft()




            if i < k-1:
                continue


            output.append(window[0][0])


        return output





if __name__ == '__main__':
    s = Solution()
    s.maxSlidingWindow([1,3,-1,-3,5,3,6,7], 3)








        