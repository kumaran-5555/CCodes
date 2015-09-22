#!/usr/bin/python3
__author__ = 'kumaran'
# https://oj.leetcode.com/problems/letter-combinations-of-a-phone-number/

class Solution():

    def __init__(self):
        self.keypad = {'2' : 'abc',
                  '3' : 'def',
                  '4' : 'ghi',
                  '5' : 'jkl',
                  '6' : 'mno',
                  '7' : 'pqrs',
                  '8' : 'tuv',
                  '9' : 'wxyz'
                }

    def _letterCombinations(self, dPos, digits, sPos, string, output):
        if dPos == len(digits):
            output.append("".join(string))
            return
        d = digits[dPos]
        for i in self.keypad[d]:
            string[sPos] = i
            self._letterCombinations(dPos+1, digits, sPos+1, string, output)



    def letterCombinations(self, digits):
        output = []
        l = len(digits)
        string = [' ']* l
        self._letterCombinations(0, digits, 0, string, output)

        return  output





if __name__ == '__main__':
    s = Solution()
    print(s.letterCombinations("23"))
