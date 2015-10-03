from collections import defaultdict

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []

        for c in s:
            if c == '(' or c == '{' or c == '[':
                stack.append(c)

            else:
                if len(stack) == 0:
                    return False

                top = stack.pop()

                if c == ')' and top != '(':
                    return False
                if c == ']' and top != '[':
                    return False
                if c == '}' and top != '{':
                    return False

        if len(stack) > 0:
            return False


        return True

