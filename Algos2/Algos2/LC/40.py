class Solution(object):

    def _combinationSum2(self, start, target, prefix):
        if target == 0:
            self.output[tuple(prefix)] = 1
            return

        if target < 0 or start >= self.n or target < self.candidates[start]:
            return


        self._combinationSum2(start+1, target, prefix)

        self._combinationSum2(start+1, target-self.candidates[start], prefix+[self.candidates[start]])





    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        self.output = {}
        self.n = len(candidates)
        self.candidates = sorted(candidates)

        self._combinationSum2(0, target, [])

        return self.output.keys()

