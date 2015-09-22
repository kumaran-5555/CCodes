#!/usr/bin/python
__author__ = 'serajago'

#!https://oj.leetcode.com/problems/combination-sum/

import time
class Solution:

    def __init__(self):
        self.output = []
        self.count = 0
        self.cache = {}
    def _combinationSum(self, cadidates, lenOfCandidates, target):

        key = ("%d_%d") % (target, lenOfCandidates)
        self.count += 1

        if key in self.cache:
            return self.cache[key]

        # use last one time
        out = []
        if target > cadidates[lenOfCandidates-1]:
            useOnce = self._combinationSum(cadidates, lenOfCandidates, target-cadidates[lenOfCandidates-1])

            out += [ i +[cadidates[lenOfCandidates-1]] for i in useOnce]

        elif target == cadidates[lenOfCandidates-1]:
            out += [[cadidates[lenOfCandidates-1] ]]



        if lenOfCandidates > 1:

            out += self._combinationSum(cadidates, lenOfCandidates-1, target)


        self.cache[key] = out

        return out


    # @param candidates, a list of integers
    # @param target, integer
    # @return a list of lists of integers
    def combinationSum(self, candidates, target):

        candidates = sorted(candidates)

        ret = self._combinationSum(candidates, len(candidates), target)
        print(self.count)
        return  ret

       # @param candidates, a list of integers
    # @param target, integer
    # @return a list of lists of integers
    def combinationSum2(self, candidates, target):
        sortedCandidates = sorted(candidates)
        ret = self.__impl(sortedCandidates, target)
        print(self.count)
        return  ret

    def __impl(self, sortedCandidatesSub, quota):
        ret = list()
        self.count += 1

        for i, c in enumerate(sortedCandidatesSub):
            if quota > (c):
                tails = self.__impl(sortedCandidatesSub[i:], quota - c)
                ret += [[c]+l for l in tails]
            elif quota == c:
                ret.append([c])
            elif quota < c:
                break

        return ret

if __name__ == '__main__':
    s = Solution()
    start = time.time()
    print(len(s.combinationSum([1,2,3,4,5,6,7,8,9,10], 80)))
    end = time.time()
    print(end-start)
    #print(s.combinationSum([1,2], 1))
