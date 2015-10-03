class Solution(object):

    def _generateParenthesis(self, n, opened, closed, prefix):

        if opened == n and closed == n:
            self.output.append(prefix)
            return

        if opened < n:
            self._generateParenthesis(n, opened+1, closed, prefix+'(')

        if opened > 0 and opened > closed:
            self._generateParenthesis(n, opened, closed+1, prefix+')')





    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        self.output = []

        self._generateParenthesis(n, 0, 0, '')

        return self.output


