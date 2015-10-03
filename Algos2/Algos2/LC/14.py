class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        i = 0

        lengths = []

        maxLength = 0

        for s in strs:
            lengths.append(len(s))

        n = len(strs)

        if n == 0:
            return ''

        reachedEnd = False


        while True:
            char = None
            for j in range(n):
                if i >= lengths[j]:
                    reachedEnd = True
                    break

                if char is None:
                    char = strs[j][i]

                elif char != strs[j][i]:
                    reachedEnd = True
                    break


                   

            if reachedEnd:
                break
            
            maxLength += 1
            i += 1

        return strs[0][:maxLength]



                

            
