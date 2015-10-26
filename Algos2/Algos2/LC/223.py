class Solution(object):

    def pointInRec(self, point, A, B, C, D):
        return point[0] >= A and point[0] <= C and point[1] >= B and point[1] <= D

    def computeArea(self, A, B, C, D, E, F, G, H):
        """
        :type A: int
        :type B: int
        :type C: int
        :type D: int
        :type E: int
        :type F: int
        :type G: int
        :type H: int
        :rtype: int
        """
        
        areaA = abs(A - C) * abs(B - D)

        areaB = abs(E - G) * abs(F - H)


        # conditions for overlap exists

        c1 = (A, B)
        c2 = (C, B)
        c3 = (C, D)
        c4 = (A, D)
        center1 = ((A + C)/2, (B+D)/2)

        c5 = (E, F)
        c6 = (G, F)
        c7 = (G, H)
        c8 = (E, H)

        center2 = ((E+G)/2, (F+H)/2)



        aOverlapsB = self.pointInRec(c1, E, F, G, H) or self.pointInRec(c2, E, F, G, H) or \
        self.pointInRec(c3, E, F, G, H) or self.pointInRec(c4, E, F, G, H) or\
        self.pointInRec(center1, E, F, G, H)

        bOverlapsA = self.pointInRec(c5, A, B, C, D) or self.pointInRec(c6, A, B, C, D) or \
        self.pointInRec(c7, A, B, C, D) or self.pointInRec(c8, A, B, C, D) or\
        self.pointInRec(center2, A, B, C, D)






        # no overlaps
        if not aOverlapsB and not bOverlapsA:
            return areaA + areaB

        x = (max(A, E), min(C, G))
        y = (max(B, F), min(D, H))


        return areaA + areaB - (abs(x[0]-x[1]) * abs(y[0]-y[1]))



        



if __name__ == '__main__':
    s = Solution()
    s.computeArea(-2,-5,1,5, -3,-3,3,3)




            
        

        