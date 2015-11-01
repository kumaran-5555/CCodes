class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        
        n = len(a)
        m = len(b)

        i = n-1
        j = m-1
        c = 0
        output = []

        while i >= 0 and j >= 0:
            if a[i] == '1' and b[j] == '1':
                if c == 1:
                    output.append('1')
                    
                else:
                    output.append('0')
                c = 1

            elif (a[i] == '1' or b[j] == '1'):
                if c == 1:
                    c = 1
                    output.append('0')
                else:
                    output.append('1')

            elif c == 1:
                c = 0
                output.append('1')
            else:
                output.append('0')

            i -= 1
            j -= 1

        while i >=0:
            if c == 1 and a[i] == '1':
                output.append('0')
                c = 1
            elif c == 1:
                output.append('1')
                c = 0
            elif a[i] == '1':
                output.append('1')
            else:
                output.append('0')
            i -= 1


        while j >= 0:
            if c == 1 and b[j] == '1':
                output.append('0')
                c = 1
            elif c == 1:
                output.append('1')
                c = 0
            elif b[j] == '1':
                output.append('1')
            else:
                output.append('0')
            j -= 1

        if c == 1:
            output.append('1')
        return ''.join(output[::-1])




