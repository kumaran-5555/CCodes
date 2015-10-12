from collections import defaultdict

class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        
        self.output = defaultdict(int)

        n = len(s)
        rVal = []

        for i in range(n-9):
            substr = s[i:i+10]


            if self.output[substr] == 1:
                rVal.append(substr)
            else:
                self.output[substr] += 1


        return rVal


