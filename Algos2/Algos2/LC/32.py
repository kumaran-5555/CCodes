class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        max = 0

        open = 0

        matched = 0

        for i in s:
            if i == '(':
                open += 1

            elif i == ')' and open <= 0:
                # over closing
                open = 0
                matched = 0
                                
            elif i == ')' and open > 1:
                # proper closing
                open -= 1
                matched += 2

            elif i == ')' and open == 1:
                matched += 2
                open -= 1

                if max < matched:
                    max = matched


        # do it in reverse order

        open = 0
        matched = 0

        for i in range(len(s)-1, -1, -1):
            if s[i] == ')':
                open += 1

            elif s[i] == '(' and open <= 0:
                open = 0
                matched = 0

            elif s[i] == '(' and open > 1:
                open -= 1
                matched += 2

            elif s[i] == '(' and open == 1:
                open -= 1
                matched  += 2
                if max < matched:
                    max = matched


        return max

if __name__ == '__main__':
    s = Solution()
    s.longestValidParentheses('((((((((((()))))))))')






