class Solution(object):
    def reverseBits(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        i = 1 << 31
        j = 1
        diff = 31



        num = 0

        while i > j:
            msb = n & i
            lsb = n & j

            msb >>= diff
            lsb <<= diff

            num |=  lsb
            num |= msb

            i >>= 1
            j <<= 1
            diff -= 2

        return num



if __name__ == '__main__':
    s = Solution()
    s.reverseBits(65536)



            
