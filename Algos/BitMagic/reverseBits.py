#!/usr/bin/python3
__author__ = 'kumaran'


class Solution():

    def _reverseBits(self, num):
        ret = 0
        for i in range(8):
            if num & (1<<i):
                ret |= (1 << (8-i-1))
        return ret

    def __init__(self):
        self.mapping = {}
        for i in range(256):
            self.mapping[i.to_bytes(1, 'little')] = self._reverseBits(i).to_bytes(1, 'little')

        for k in self.mapping:
            print(k,self.mapping[k])



    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        bytesArray = n.to_bytes(4, 'little')
        reversedBytes = bytesArray[::-1]
        reversedBytesNew = []

        for i in range(len(reversedBytes)):
            reversedBytesNew.append(self.mapping[reversedBytes[i].to_bytes(1,'little')])


        return ''.join(reversedBytesNew[::-1])




if __name__ == '__main__':
    s = Solution()
    print(s.reverseBits(1))
    
