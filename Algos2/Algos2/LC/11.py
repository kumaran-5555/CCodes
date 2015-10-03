class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        n = len(height)

        if n == 0 or n == 1:
            return 0


        i = 0
        j = n-1

        maxVol = 0

        while i < j:
            vol = min(height[i], height[j]) * (j - i)

            if maxVol < vol:
                maxVol = vol

            if height[i] <= height[j]:
                # we will move left
                while i+1 < n and height[i+1] <= height[i]:
                    i += 1

                i += 1

            else:
                # we will move right
                while j-1 >= 0 and height[j-1] <= height[j]:
                    j -= 1

                j -= 1

        return maxVol



if __name__ == '__main__':
    s = Solution()

    print(s.maxArea([1,2,3,4,5,6]))
    print(s.maxArea([1,2,3,4,5,2,3,4,7,4,1,2,3]))