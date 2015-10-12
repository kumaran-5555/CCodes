class Solution(object):
    @staticmethod
    def compareFunc(n1, n2):
        s1 = str(n1) + str(n2)
        s2 = str(n2) + str(n1)

        i = 0
        j = 0

        l1 = len(s1)
        l2 = len(s2)

        while i < l1 and j < l2:
            if s1[i] > s2[j]:
                return 1

            elif s1[i] < s2[j]:
                return -1

            i += 1
            j += 1

        return 0





    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        

        return  ''.join([str(i) for i in nums.sort(compare=compareFunc)])




        