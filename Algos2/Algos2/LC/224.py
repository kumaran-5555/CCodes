class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        # no precendence because only +,- is allowed

        # parse

        expression = []

        start = 0




        s = s.replace(' ','')
        s = s.replace(')','')
        s = s.replace('(', '')

        n = len(s)
        if n == 0:
            return 0

        for i in range(1, n):
            if s[i] == '+' or s[i]  == '-':
                expression.append(s[start:i])
                
                if s[i] == '+' or  s[i] == '-':
                    expression.append(s[i])

                start = i+1
        expression.append(s[start:])
        total = int(expression[0])
        n = len(expression)
        i = 1

        while i < n:
            if expression[i] == '+':
                total += int(expression[i+1])
                i += 2
            elif expression[i] == '-':
                total -= int(expression[i+1])
                i += 2

        return total



if __name__ == '__main__':
    s = Solution()
    s.calculate("      ")



