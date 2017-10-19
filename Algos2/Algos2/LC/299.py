from collections import defaultdict

class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """

        bulls = 0
        cows = 0
        secret = list(secret)
        guess = list(guess)
        s = defaultdict(lambda : 0)
        g = defaultdict(lambda : 0)
        for i in range(len(secret)):
            if secret[i] == guess[i]:
                bulls += 1
                secret[i] = None
                guess[i] = None
                continue        

            g[guess[i]]+=1


            
        for i in range(len(secret)):
            if secret[i] == None:
                continue
            
            if g[secret[i]] > 0:
                cows += 1
                g[secret[i]] -= 1
        
            
        return '{}A{}B'.format(bulls, cows)
        
            
            