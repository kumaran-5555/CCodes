class Solution(object):
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        
        self.result = []
        self.minRemoved = len(s)
        self.remainingCloseAtPos = [0] * len(s)
        count = 0
        for i in range(len(s)-1,0,-1):
            if s[i] == ')':
                count+=1
            self.remainingCloseAtPos[i-1] = count
        
        self.tryRemove(s, 0, 0, 0, '')
        


        return list(set(self.result))




    
    def tryRemove(self, s, cursorPos, numOpen, numRemoved, newString):

        if numRemoved > self.minRemoved:
            return

        if len(s) == cursorPos:
            # reached end            
            if numOpen == 0:
                # balanced
                if self.minRemoved < numRemoved:
                    # this not the best
                    return
                elif self.minRemoved == numRemoved:
                    self.result.append(newString)
                else:
                    self.result = []
                    self.result.append(newString)
                    self.minRemoved = numRemoved

            else:
                # imbalanced
                return
        
        else:
            if s[cursorPos] != '(' and s[cursorPos] != ')':
                self.tryRemove(s, cursorPos+1, numOpen, numRemoved, newString + s[cursorPos])
            else:
                if s[cursorPos] == ')':
                    if numOpen == 0:
                        # we can't keep this, has to be removed
                        self.tryRemove(s, cursorPos+1, numOpen, numRemoved+1, newString)
                    else:
                        # we can either keep or remove
                        # remove
                        self.tryRemove(s, cursorPos+1, numOpen, numRemoved+1, newString)
                        # keep
                        self.tryRemove(s, cursorPos+1, numOpen-1, numRemoved, newString + s[cursorPos])
                else:
                    if self.remainingCloseAtPos[cursorPos] < numOpen:
                        # we don't have enough closing, we have to remove
                        # remove
                        self.tryRemove(s, cursorPos+1, numOpen, numRemoved+1, newString)

                    else:
                        # keep
                        self.tryRemove(s, cursorPos+1, numOpen+1, numRemoved, newString + s[cursorPos])
                        # remove
                        self.tryRemove(s, cursorPos+1, numOpen, numRemoved+1, newString)

    

if __name__ == '__main__':
    c = Solution()
    c.removeInvalidParentheses("(a)())()")
    print(c.result)
