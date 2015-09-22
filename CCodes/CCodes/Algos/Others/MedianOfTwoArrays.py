#!/usr/bin/python3
__author__ = 'kumaran'

class Solution():


    def returnMedian(self, a, i, b, j, isEven):
        if isEven:
            if i==-1:
                # we dont need any element from a
                return float(b[j]+b[j-1]) /2
            elif j==0:
                # have to use a[i]
                return float(a[i] + b[j]) / 2
            else:
                # check if a[i] precedes b[j] or b[j-1] preceds b[j]
                if a[i] >= b[j-1]:
                    return float(a[i]+b[j]) /2
                else:
                    return float(b[j]+b[j-1]) /2

        else:
            return  b[j]

    def medianInB(self, a, b, elementsBeforeMedian, isEven):
        s = 0
        e = len(b) - 1
        while s <= e:
            #print(s,e)
            j = s + (e-s+1) // 2
            i = (elementsBeforeMedian - j - 1)

            # for b[j] to be median, it need a[0:i+1] elements to be lower than b[j]

            if i > len(a)-1:
                # chossen small elements from B, can't have i elements from a
                s = j + 1
            elif i < -1:
                # choosen more elements from B than needed
                # j is more than media
                e = j - 1
            elif i == -1:
                # don't need any element from a
                if b[j] <= a[0]:
                    # j is median and needs zero elements from a
                    # found
                    return  self.returnMedian(a, i, b,j, isEven)
                elif b[j] > a[0]:
                    # j is more than median
                    e = j - 1

            elif i == len(a) - 1:
                # need all element from a
                if b[j] >= a[len(a)-1]:
                    # j is median
                    # found
                    return self.returnMedian(a, i, b,j, isEven)
                elif b[j] < a[len(a)-1]:
                    # j is less than median
                    s = j + 1
            elif a[i] <= b[j] and b[j] <= a[i+1]:
                # j is median
                # found
                return self.returnMedian(a, i, b,j, isEven)
            elif a[i] <= b[j] and a[i+1] <= b[j]:
                # j is more than median
                e = j - 1
            elif a[i] >= b[j] and a[i+1] >= b[j]:
                # j is less than median
                s = j + 1

        return  None

    # @return a float
    def findMedianSortedArrays(self, A, B):

        totalLen = len(A) + len(B)
        isEven = (totalLen % 2) == 0
        elementsBeforeMedian = (totalLen) // 2

        if not len(A):
            if isEven:
                return float(B[elementsBeforeMedian] + B[elementsBeforeMedian-1] ) / 2
            else:
                return B[elementsBeforeMedian]
        if not len(B):
            if isEven:
                return float(A[elementsBeforeMedian] + A[elementsBeforeMedian-1]) / 2
            else:
                return A[elementsBeforeMedian]



        median = self.medianInB(A,B, elementsBeforeMedian, isEven)
        if median:
            return median

        return self.medianInB(B, A, elementsBeforeMedian, isEven)


if __name__ == '__main__':
    s = Solution()
    #print(s.findMedianSortedArrays([1,2],[1,2]))
    #print(s.findMedianSortedArrays([],[1,2,3,4,5,6]))
    #print(s.findMedianSortedArrays([1],[1]))
    #print(s.findMedianSortedArrays([3],[1,2,4]))
    #print(s.findMedianSortedArrays([1,3],[2,4]))
    #print(s.findMedianSortedArrays([4],[1,2,3,5,6]))
    #print(s.findMedianSortedArrays([1],[2,3,4]))
    print(s.findMedianSortedArrays([5],[1,2,3,4,6]))