class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        
        stack = []

        if len(tokens) == 0:
            return 0


        for i in tokens:
            if i != '*' and i != '+' and i != '-' and i != '/':
                stack.append(int(i))

            elif i == '*':
                right = stack.pop()
                left = stack.pop()
                stack.append(left * right)

            elif i == '/':
                right = stack.pop()
                left = stack.pop()
                stack.append(int(float(left) / right))

            elif i == '+':
                right = stack.pop()
                left = stack.pop()
                stack.append(right + left)

            elif i == '-':
                right = stack.pop()
                left = stack.pop()
                stack.append(left - right)

        return stack[0]