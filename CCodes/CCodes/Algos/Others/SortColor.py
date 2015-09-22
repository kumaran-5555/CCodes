# https://oj.leetcode.com/problems/sort-colors/

class Solution()
    def swap(self, A, p1, p2):
        temp = A[p1]
        A[p1] = A[p2]
        A[p2] = temp

    def sortColors(self, A):
        l = len(A)
        zero = 0
        two = l-1
        while (A[zero] == 0 and zero < l):
            zero += 1
        while(A[two]==2 and two >= 0):
            two -= 1
        for i in range(l):
            if A[i] == 0:
                self.swap(A, zero, i)
                zero += 1
                while (A[zero] == 0 and zero < l):
                    zero += 1
            elif A[i] == 1:
                continue
            elif A[i] == 2 and two > i:
                self.swap(A, i, two)
                two -= 1
                while(A[two]==2 and two >= 0):
                    two -= 1
                # check swapped is zero
                if A[i] == 0:
                    self.swap(A, zero, i)
                    zero += 1
                    while (A[zero] == 0 and zero < l):
                        zero += 1
