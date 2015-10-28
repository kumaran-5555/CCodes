from collections import defaultdict

class Solution(object):

    def getKey(self, str):
        key = [0]*27
        for c in str:
            key[ord(c)-ord('a')] += 1

        return key
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        strs = sorted(strs)

        keysMap = defaultdict(list)

        for s in strs:
            keysMap[tuple(self.getKey(s))].append(s)

        output = []


        for k in keysMap:
            output.append(keysMap[k])


        return output



