class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        words = s.strip().split()

        out = ''

        

        for i in range(len(words)-1,-1,-1):
            if out == '':
                out = words[i]
            else:
                out += ' '+words[i]


        return out

