class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        output = ''


        row = 0
        i = 0
        n = len(s)

        if numRows == 1:
            return s

        while row < numRows:
            i = 0
            while i < n:

                if row == 0:
                    output += s[i]
                   
                elif row == numRows - 1:

                    if i + row >= n:
                        break

                    output += s[i + row]

                else:

                    if i + row >= n:
                        break

                    output += s[i + row]

                    if i + (2 * numRows) - 2 - row >= n:
                        break

                    output += s[i + (2 * numRows) - 2 - row]

                i += (2 * numRows) - 2

            row += 1


        return output


if __name__ == '__main__':
    s = Solution()
    r = s.convert('PAYPALISHIRING', 4)
    print(r)

