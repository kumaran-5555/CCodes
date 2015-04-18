__author__ = 'serajago'



class FoldingPaper2:
    def solve(self, W, H, A):
        factors = [[i,A//i] for i in range(2, A//2) if A%i == 0]

        minMoves = float('inf')
        for f in factors:
            # steps to reach H
            x=f[0]
            y=f[1]
            toReachH = 0
            while x < H:
                toReachH += 1
                x *= 2
            toReachW = 0
            while y < W:
                toReachW += 1
                y *= 2
            minMoves = min(minMoves, toReachH + toReachW)

            x=f[0]
            y=f[1]
            toReachH = 0
            while y < H:
                toReachH += 1
                y *= 2
            toReachW = 0
            while x < W:
                toReachW += 1
                x *= 2

            minMoves = min(minMoves, toReachH + toReachW)

        if minMoves == float('inf'):
            return  -1
        return minMoves







if __name__ == '__main__':
    s = FoldingPaper2()
    print(s.solve(5,3,12))
    print(s.solve(127,129,72))