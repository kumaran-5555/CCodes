class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
       
        maxCitations = 0
        n = len(citations)
        if n == 0:
            return 0


        start = 0
        end = n-1

        while start <= end:

            i = start + (end - start)//2

            if citations[i] <= n-i:
                # we have more width but less citations, go right to get more citations
                c = citations[i]

                start = i+1
                
            elif n-i < citations[i]:
                # we have more width but less citations, go left to get more width
                c = n-i

                end = i-1

            if maxCitations < c:
                maxCitations = c


        return maxCitations



if __name__ ==  '__main__':
    s = Solution()
    #print(s.hIndex([1,1,1,1,1,2,2,2,2,2,2,3,3,3,3,3,3,4,4,4,4,4,5,5,5,5,5,5]))3, 0, 6, 1, 5
    print(s.hIndex([0,1,3,5,6]))
