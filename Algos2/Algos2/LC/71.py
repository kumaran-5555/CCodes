class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        

        outputPath = ''

        fields = path.split('/')

        stack = []

        for f in fields[1:]:
            if f == '.' or f == '':
                continue

            if f == '..':
                if len(stack):
                    stack.pop()
                continue

            stack.append(f)

        if len(stack) == 0:
            return "/"
        
        for f in stack:
            outputPath += '/' + f
        
        
        
        return outputPath


if __name__ == '__main__':
     s = Solution()

     s.simplifyPath( "/../")