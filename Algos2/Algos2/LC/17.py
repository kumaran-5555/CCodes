class Solution(object):

    def getAllCombinations(self, digits, i, prefixes):

        if i == len(digits):
            for p in prefixes:
                self.output.append(p)
            return

        result = []
        for c in self.pad[digits[i]]:
            for p in prefixes:
                result.append(p + c)

        self.getAllCombinations(digits, i+1, result)



    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        self.output = []
        if len(digits) == 0:
            return []
        self.pad = { '2': 'abc', '3':'def', '4':'ghi',
                    
                    '5': 'jkl', '6': 'mno', '7': 'pqrs', '8':'tuv', '9':'wxyz'}


        self.getAllCombinations(digits, 0, [''])

        return self.output

