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
        
        n = len(s)
        if n == 0:
            return 0

        temp = ''
        for c in s:
            if c == '+' or c == '-' or c == ')' or c == '(':
                if temp != '':
                    expression.append(int(temp))
                    temp = ''
                expression.append(c)
            else:
                temp += c

        if temp != '':
            expression.append(int(temp))



        stack = []



        for e in expression:
            if e == '(':
                stack.append(e)
                continue

            elif e == '+' or e == '-':
                stack.append(e)

            elif e == ')':

                num = stack.pop()

                open = stack.pop()

                # check for operator
                if len(stack):
                    operator = stack.pop()
                    lh = stack.pop()

                    if operator == '+':
                        stack.append(num + lh)
                    else:
                        stack.append(lh - num)
                else:
                    stack.append(num)

                                  



            else:
                if len(stack) and stack[-1] != '(':
                    operator = stack.pop()
                    lh = stack.pop()

                    if operator == '+':
                        stack.append(e + lh)
                    else:
                        stack.append(lh - e)

                else:
                    stack.append(e)



        return stack[-1]




if __name__ == '__main__':
    s = Solution()
    s.calculate("1 + 1")



