

def binarySearch(arr, val):
    l = 0
    h = len(arr)-1

    while l < h:
        m = (h-l)//2 + 1 + l

        if arr[m] <  val:
            l = m
        else:
            h = m-1

    if arr[l] < val:
        return l
    else:
        return -1






            




class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0

        lis = []
        lis.append(nums[0])

        for n in nums[1:]:
            i = binarySearch(lis, n)

            if len(lis) > i+1:
                lis[i+1] = n
            else:
                lis.append(n)

        return len(lis)

                    
        


if __name__ == '__main__':
    c = Solution()
    print(c.lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18]))
