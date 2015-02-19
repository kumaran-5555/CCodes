#https://oj.leetcode.com/problems/jump-game/
class Solution:
    # @param A, a list of integers
    # @return a boolean
    def canJump(self, A):
        l1 = len(A)
        
        if l1 == 1:
            return True
            
        zerothPosition = None
        
        for i in range(l1-1, -1, -1):
            if zerothPosition is None:
                if A[i] == 0:
                    zerothPosition = i
                continue
            else:
                val = A[i]
                distance = zerothPosition - i
                if zerothPosition == l1-1:
                    # just reachin is enoough
                    if val >= distance:
                        zerothPosition = None
                
                elif val > distance:
                    zerothPosition = None
                    
        if zerothPosition is not None:
            return False
            
        return True
        
