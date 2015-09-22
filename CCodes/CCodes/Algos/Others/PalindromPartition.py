class Solution:
    def __init__(self):
        self.minCount = []

    def doEvenPalindrome(self, s, position):
        # current position forms the first left of palindrom of length2
        i=1
        while position-(i-1) >= 0 and position+i <= len(s)-1:
            if s[position-(i-1)] == s[position+i]:
                self.minCount[position-(i-1)] = min(self.minCount[position-(i-1)], self.minCount[position+i+1] +1)
            else:
                return
            i += 1

    def doOddPalindrome(self, s, position):
        i=0
        while position+i <= (len(s)-1) and position-i >= 0:
            if s[position+i] == s[position-i]:
                # use this palindrom or not
                # if we use, the total count is the previous count + 1
                self.minCount[position-i] = min(self.minCount[position-i], 1 + self.minCount[position+i+1])
            else:
                return

            i += 1

    # @param s, a string
    # @return an integer
    def minCut(self, s):
        # holds # of min palindrome count
        # go till 0 for sentinal
        self.minCount = [i for i in range(len(s),-1,-1)]
        #print(self.minCount)
        for i in range(len(s)-1,-1,-1):
            self.doEvenPalindrome(s, i)
            self.doOddPalindrome(s, i)
        #print(self.minCount)
        return self.minCount[0]-1
