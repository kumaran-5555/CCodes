from collections import defaultdict

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        
        sDict = defaultdict(int)
        tDict = defaultdict(int)

        n = len(s)
        m = len(t)
        if n != m:
            return False

        for i in range(n):
            sDict[s[i]] += 1
            tDict[t[i]] += 1

        for c in sDict:
            if c not in tDict or sDict[c] != tDict[c]:
                return False

        return True






