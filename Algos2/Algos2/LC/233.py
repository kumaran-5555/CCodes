class Solution(object):
    def countDigitOne(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        if n < 0:
            return 0
            
        countsBefore = [0] * 50
        countsBefore[1] = 1

        multiple = 10
        for i in range(2, 50):
            countsBefore[i] = countsBefore[i-1] * 10 + multiple

            multiple *= 10


        restTheNumber = 0
        multiple = 1
        total = 0
        position = 0

        while n:
            x = n % 10

            if x > 1:
                total += (countsBefore[position] * x) + multiple
            elif x == 1:
                total += (countsBefore[position] + restTheNumber + 1)

            restTheNumber += (x  * multiple)

            n //= 10

            position += 1
            multiple *= 10

        return total



if __name__ == '__main__':
    s = Solution()
    s.countDigitOne(2784)
            


