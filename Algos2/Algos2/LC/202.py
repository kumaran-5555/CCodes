class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        
        self.prev = {}
        self.prev[n] = 1


        while n != 1:
            next = 0

            mod = 10

            while n:
                next += ((n % mod) ** 2)

                n /= 10

            n = next

            if n in self.prev:
                return False

            self.prev[n] = 1

        return True
            

