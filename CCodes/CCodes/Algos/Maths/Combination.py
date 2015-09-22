#!/usr/bin/python3
__author__ = 'kumaran'


class Solution:

    def __init__(self):
        self.integers = []


    def numBits(self, n):
        count = 0
        while n:
            n &= n-1
            count += 1
        return count

    def getIntegers(self, num, bits):
        output = []

        for i in range(bits):
            if num & (1 << i):
                output.append(self.integers[i])

        return output


    # @return a list of lists of integers
    def combine(self, n, k):
        output = []
        # n is num bits
        self.integers = [i for i in range(1,n+1)]
        # iterate throuh 1 to 2**n
        for i in range(1, (2**n)):
            # if number of bits set in i is k, (n_c_k)
            if self.numBits(i) == k:
                # get corresponding output
                output.append(self.getIntegers(i, n))

        return output


if __name__ == '__main__':
    s = Solution()
    print(s.combine(4,3))







if __name__ == '__main__':
    s = Solution()
    
