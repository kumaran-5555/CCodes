class Solution(object):

    def hasMedian(self, l1, l2):
        # we will search for median in l1

        start = 0
        n = len(l1)
        m = len(l2)
        end = n - 1
        
        while start <= end:
            i = start + (end - start)//2

            j = (n + m)//2 - i - 1

            if j >= m:
                # we are asking for from another list
                # which doesn't have enough, go right
                start = i + 1
                continue

            elif j < -1:
                end = i - 1
                continue



            if (j < 0 or l2[j] <= l1[i]) and (j+1 >= m or l2[j+1] >= l1[i]):
                return i
            elif (j < 0 or l2[j] > l1[i]) and (j+1 >= m or l2[j+1] > l1[i]):
                # both of them are larger, need more 
                start = i + 1

            elif (j < 0 or l2[j] < l1[i]) and (j+1 >= m or l2[j+1] < l1[i]):
                # need less
                end = i - 1

        return -1


    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        
        n = len(nums1)
        m = len(nums2)

        

        isOdd = ((n + m) % 2) == 1

        if m == 0 and n > 0:
            if isOdd:
                return nums1[n//2]
            else:
                return (nums1[n//2 - 1] + nums1[n//2]) / 2

        elif n == 0 and m > 0:
            if isOdd:
                return nums2[m//2]
            else:
                return (nums2[m//2 - 1] + nums2[m//2]) / 2


        while True:

            median = self.hasMedian(nums1, nums2)

            # for even caes, we have right side element
            # left side could be coming from either side
            if median != -1:
                if isOdd:
                    return nums1[median]
                else:
                    j = (n + m) // 2 - median - 1

                    if j < 0:
                        # we don't want anything from list2
                        return float((nums1[median-1] + nums1[median])) / 2

                    elif median > 0 and nums2[j] < nums1[median-1]:
                        return float((nums1[median-1] + nums1[median])) / 2
                    else:
                        return float((nums2[j] + nums1[median]))/2

            temp = nums1
            nums1 = nums2
            nums2 = temp

                

if __name__ == '__main__':
    s = Solution()
    
    t = s.findMedianSortedArrays([], [2,3])
    print(t)








