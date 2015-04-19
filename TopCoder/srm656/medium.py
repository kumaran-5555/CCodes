__author__ = 'serajago'


class RandomPancakeStackDiv2:
    def _expected(self, n, choosen, delicious):
        totalLeftOut = sum([1 for i in choosen if not i])
        if not totalLeftOut:
            return 0

        expected = 0
        expected = 1/totalLeftOut * sum([1 for i in range(len(choosen)) if i > n and not choosen[i]]) * delicious

        for i in range(n):
            if choosen[i]:
                continue
            choosen[i] = True
            expected += (1/totalLeftOut * self._expected(i, choosen, delicious+self.d[i]))
            choosen[i] = False

        return expected




    def expectedDeliciousness(self, d):
        n = len(d)
        self.dpTable = [-1]*n
        self.d = d
        choosen = [False] * n
        return  self._expected(n, choosen, 0)


if __name__ == '__main__':
    s =RandomPancakeStackDiv2()
    s.expectedDeliciousness([1,1,1,1,1,1,1,1,1,1])


