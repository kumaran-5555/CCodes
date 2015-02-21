#!/usr/bin/python3
__author__ = 'kumaran'


class Solution():
    def longestValidParentheses(self, s):
        maxPair = 0
        currentPairCount = 0
        # stores the pair count before staring a nesting level
        nestedOpenCount = []
        nested = 0
        for i in s:
            if i == ')':
                if nested:
                    currentPairCount += 1
                    # add the number of matching pair just before this nesting level
                    currentPairCount += nestedOpenCount.pop()
                    if currentPairCount > maxPair:
                        maxPair = currentPairCount

                    nested -= 1

                else:
                    nestedOpenCount = []
                    currentPairCount = 0
                    nested = 0

            elif i == '(':
                nestedOpenCount.append(currentPairCount)
                # starte new nesting level, so reset the previous matching pair count to zero
                currentPairCount = 0
                nested += 1

        return maxPair * 2



if __name__ == '__main__':
    s = Solution()
    print(s.longestValidParentheses("()(()"))
