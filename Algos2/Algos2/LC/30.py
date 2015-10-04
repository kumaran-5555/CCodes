
from collections import defaultdict

class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        
        allWords = defaultdict(int)


        for w in words:
            allWords[w] += 1




        currWords = {}

        self.output = []

        n = len(s)
        m = len(words)

        if m == 0 or n == 0:
            return []


        k = len(words[0])

        i = 0
        while (i + (m * k)) <= n:


            currWords = defaultdict(int)
            count = 0
            j = i

            while j+k <= n and count < m:
                w = s[j:j+k]

                if w in allWords and currWords[w] < allWords[w]:
                    currWords[w] += 1
                    count += 1
                    j += k
                else:
                    break

            if count == m:
                self.output.append(i)


            i += 1

        return self.output

if __name__ == '__main__':
    s = Solution()

    s.findSubstring( "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
, ['a','a','a','a'] )

            

