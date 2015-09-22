from collections import deque

# https://oj.leetcode.com/problems/minimum-window-substring/
class Solution:
    # @return a string
    # @return a string
    def minWindow(self, S, T):
        minIdx = {}
        count = {}
        queue = {}
        currCount = {}
        currTotal = 0
        total = len(T)
        maxIdx = None
        minWindowSize = len(S) + 1
        minWindowLeft = None
        minWindowRight = None

        for c in T:
            if c in count:
                count[c] += 1
            else:
                count[c] = 1
                currCount[c] = 0

        for c in count:
            if count[c] > 1:
                queue[c] = deque()

        for i in range(len(S)):
            c = S[i]
            if c not in count:
                # not interested
                continue

            if count[c] > currCount[c]:
                # don't have all words in window yet
                currCount[c] += 1
                currTotal += 1
                maxIdx = i

                if currCount[c] == 1:
                    # update min, if we are seeing for the first time
                    minIdx[c] = i

                if count[c] > 1:
                    # update multi words in queue
                    queue[c].append(i)

            else:
                # have all in window, just update window
                if count[c] == 1:
                    minIdx[c] = i
                else:
                    # remove exiting min
                    queue[c].popleft()

                    # add current at the end
                    queue[c].append(i)

                    # take next as min
                    minIdx[c] = queue[c][0]
                maxIdx = i

            if total == currTotal:
                currMin = min(minIdx.values())
                if minWindowSize > (maxIdx - currMin + 1):
                    minWindowSize = (maxIdx - currMin + 1)
                    minWindowLeft = currMin
                    minWindowRight = maxIdx

        if minWindowLeft is None:
            return  ""

        return S[minWindowLeft:minWindowRight+1]
