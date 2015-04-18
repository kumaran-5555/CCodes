__author__ = 'serajago'

from collections import defaultdict
class NineEasy:

    def  _count(self, sums, digitPos, sum2):
        print(sums, digitPos, self.numDigits)
        key = "_".join([str(i) for i in  sums])+"_"+str(digitPos)
        if key in self.dpTable:

            return self.dpTable[key]

        if digitPos == self.numDigits and sum(sums) == 0:
            return 1
        elif digitPos == self.numDigits:
            return 0


        # try all digits for this position
        for i in range(0,10):
            # update sums for each question
            newSums = sums[:]
            newSum2 = 0
            for j in range(self.N):
                if self.d[digitPos] & (1<<j):
                    newSums[j] = (newSums[j] + i) % 9
            # try next position key this position as a digit
            self.dpTable[key] = (self.dpTable[key] + self._count(newSums, digitPos+1)) % self.mod


        return  self.dpTable[key]






    def count(self, N, d):
        # key = s1_s2_s3_s4_s5_digitPos
        # val = count
        self.dpTable = defaultdict(int)
        self.N = N
        self.d = d
        self.numDigits = len(d)
        self.mod = 1000000007
        sums = [0] * (self.N)
        self._count(sums, 0)
        print(self.dpTable)
        return  self.dpTable["_".join(["0"]*(self.N+1))]




if __name__ == '__main__':
    s = NineEasy()
    print(s.count(1,[0,0,1]))