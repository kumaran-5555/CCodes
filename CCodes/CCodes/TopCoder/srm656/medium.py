
    class RandomPancakeStackDiv2:
        def _expected(self, n, numChoosen):

            if self.dpTable[n][numChoosen] != -1:
                return self.dpTable[n][numChoosen]
            totalLeftOut = self.n - numChoosen
            if not totalLeftOut:
                return 0

            expected = 0
            #expected = 1/totalLeftOut * (self.n -n - numChoosen)

            for i in range(n):
                #if choosen[i]:
                #    continue
                #choosen[i] = True
                print(i)
                expected += (1/totalLeftOut * (self.d[i] + self._expected(i, numChoosen+1)))
                #choosen[i] = False
            self.dpTable[n][numChoosen] = expected
            return expected




        def expectedDeliciousness(self, d):
            self.n = len(d)
            n = len(d)
            self.dpTable = []
            for i in range(n+2):
                self.dpTable.append([-1]*(n+2))

            self.d = [0]+list(d)
            choosen = [False] * n
            return  self._expected(n+1, 0)



    s =RandomPancakeStackDiv2()
    s.expectedDeliciousness([1,1,1,1,1,1,1,1,1,1])
