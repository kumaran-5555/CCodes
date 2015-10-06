import datetime



class Solution(object):

    def _combinationSum(self, candidates, start, target, prefix):

        
        if start >= self.n or target < 0:
            return 


        if target == 0:
            self.output.append(prefix)
            return

        if candidates[start] > target:
            return


        # don't use current value
        # skip all duplicates
        i = start
        while i+1 < self.n and candidates[i] == candidates[i+1]:
            i += 1

        self._combinationSum(candidates, i+1, target, prefix)

        # use the current value
        self._combinationSum(candidates, start, target-candidates[start], prefix + [candidates[start]])




    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        
        self.output = []
        self.dp = {}
        self.n = len(candidates)

        candidates = sorted(candidates)

        self._combinationSum(candidates, 0, target, [])

        return self.output

if __name__ == '__main__':
    s = Solution()
    l1 = [i for i in range(1,25)]
    target = 30
    start = datetime.datetime.now()

    s.combinationSum(l1, target)

    print(datetime.datetime.now() - start)
