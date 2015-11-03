class Solution(object):

    def _restoreIp(self, pos, prefix, l):
        if pos == self.n and l == 4:
            self.output.append('.'.join(prefix))
            return

        for i in range(pos, min(pos+3, self.n)):
            octet = int(self.s[pos:i+1])

            if octet > 255:
                # can't try further
                break

            self._restoreIp(i+1, prefix + [self.s[pos:i+1]], l+1)

            if octet == 0:
                # can't try further
                break

        return




            
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        

        self.n = len(s)
        self.output = []
        self.s = s


        if self.n < 4 or self.n > 12:
            return []

        
        self._restoreIp(0, [], 0)

        return self.output
