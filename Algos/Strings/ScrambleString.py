#!/usr/bin/python3
__author__ = 'kumaran'


class Solution():
    def _isScramble(self, a, b):


        # check it is equal in the interval
        if a == b:
            return True
        # if string are not same size
        if len(a) != len(b):
            return False
        # if string are single char, no children to scramble
        if len(a) == 1:
            return False

        # iterator over non empty substrings of length i
        for i in range(1, len(a)):
            a1 = a[:i]
            a2 = a[i:]
            a12 = a[:len(a)-i]
            a22 = a[len(a)-i:]

            b1 = b[:i]
            b2 = b[i:]
            b12 = b[:len(a)-i]
            b22 = b[len(a)-i:]

            print(a,b)
            print(a1,b1)
            print(a2,b2)
            print(a12, b22)
            print(a22, b12)
            #self._isScramble(a1, b1) and self._isScramble(a2, b2)

            #self._isScramble(a12, b22) and self._isScramble(a22, b12)






    def isScramble(self, s1, s2):
        return self._isScramble(s1, s2)


if __name__ == '__main__':
    s = Solution()
    print(s.isScramble("abb", "bba"))
    #print(s.isScramble("a", "a"))
    #print(s.isScramble("ab", "ba"))
    #print(s.isScramble("abc", "cba"))
    #print(s.isScramble("ate", "eta"))
    #print(s.isScramble("ate", "eat"))
    #print(s.isScramble("ate", "tae"))