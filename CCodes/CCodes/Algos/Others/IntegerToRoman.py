#!/usr/bin/python3
__author__ = 'kumaran'


class Solution:
    # @return a string
    def intToRoman(self, num):
        output = ""
        alphabets = ['I', 'V', 'X', 'L', 'C', 'D', 'M']
        '''
        F - is current alphabet
        N - next alphabet
        M - next to next alphabet
        '''
        patterns = {1 : 'F',
                    2: 'FF',
                    3: 'FFF',
                    4: 'FN',
                    5: 'N',
                    6: 'NF',
                    7: 'NFF',
                    8: 'NFFF',
                    9: 'FM'}

        position = 0
        n = num
        while n > 0:
            val = n % 10
            if val == 0:
                n //= 10
                position += 2
                continue
            p = patterns[val]
            p = p.replace('F', alphabets[position])
            if position < len(alphabets)-1:
                p = p.replace('N', alphabets[position+1])
            if position < len(alphabets)-2:
                p = p.replace('M', alphabets[position+2])

            output = p + output
            position += 2
            n //= 10

        return  output


if __name__ == '__main__':
    s = Solution()
    
