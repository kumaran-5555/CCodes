class Solution(object):
    def evaluate(self, expression):
        output = 0
        n = len(expression)

        if n == 0:
            return 0

        stack = []
        stack.append(expression[0])

        i = 1
        while i < n:
            if expression[i] == '*':
                l = int(stack.pop())
                r = int(expression[i+1])

                stack.append(l * r)

                i += 2
            else:
                stack.append(expression[i])
                i += 1

        n = len(stack)

        output = int(stack[0])
        i = 1
        sign = 1
        while i < n:
            if stack[i] == '+':
                sign = 1
            elif stack[i] == '-':
                sign = -1

            else:
                output += (sign * int(stack[i]))
            i += 1

        return output






    def _addOperators(self, start, end, expression):

        if start > end:
            if self.evaluate(expression) == self.target:
                self.output.append(expression)
                return
            else:
                return


        for i in range(start, end+1):
            num = self.num[start:i+1]
                        

            if i < end:
                # can add operator
                self._addOperators(i+1, end, expression + [num, '+'])
                self._addOperators(i+1, end, expression + [num, '-'])
                self._addOperators(i+1, end, expression + [num, '*'])
            else:
                self._addOperators(i+1, end, expression + [num])

            if num == '0':
                break



            









        

    def addOperators(self, num, target):
        """
        :type num: str
        :type target: int
        :rtype: List[str]
        """
        
        self.num = num
        self.target = target

        self.output = []
        self.tempExpression = []
        self._addOperators(0, len(num)-1, [])


        return self.output







if __name__ == '__main__':
    s = Solution()
    s.addOperators("3456237490", 9191 )

