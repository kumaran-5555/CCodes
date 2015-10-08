class Solution(object):
    def _diffWaysToCompute(self, input, start, end):

        if start > end:
            return []

        if start == end:
            return [int(input[start])]

        output = []

        for i in range(start+2, end+1, 2):
            leftOut = self._diffWaysToCompute(input, start, i-2)
            rightOut = self._diffWaysToCompute(input, i, end)

            for k in leftOut:
                for m in rightOut:
                    if input[i-1] == '+':
                        output.append(k + m)
                    elif input[i-1] == '-':
                        output.append(k - m)
                    elif input[i-1] == '*':
                        output.append(k * m)

        return output

    


    def diffWaysToCompute(self, input):
        """
        :type input: str
        :rtype: List[int]
        """
        
        l = []

        i = 0
        j = 0
        n = len(input)
        while j < n:
            while j < n and input[j] != '+' and input[j] != '-' and input[j] != '*':
                j += 1

            l.append(input[i:j])
            if j < n:
                l.append(input[j])
            j += 1
            i = j




        output = self._diffWaysToCompute(l, 0, len(l)-1)

        return sorted(output)


if __name__ == '__main__':

    s = Solution()
    s.diffWaysToCompute("12*3-14*5")