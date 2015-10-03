class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        citations = sorted(citations)
        maxCitations = 0
        n = len(citations)

        for i in range(n):
            if citations[i] <= n-1:
                c = citations[i]
            elif n-1 < citations[i]:
                c = n-1

            if maxCitations < c:
                maxCitations = c


        return maxCitations

