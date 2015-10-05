class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        words = str.split(' ')

        self.mapping = {}
        self.mappingWords = {}

        n = len(words)

        if n != len(pattern):
            return False


        i = 0
        for c in pattern:


            if c not in self.mapping and words[i] not in self.mappingWords:
                self.mapping[c] = words[i]
                self.mappingWords[words[i]] = c

            elif c not in self.mapping or words[i] not in self.mappingWords:
                return False

            elif self.mapping[c] != words[i] or self.mappingWords[words[i]] != c:
                return False





            i += 1

        return True



