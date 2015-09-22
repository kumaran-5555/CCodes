#!/usr/bin/python3
__author__ = 'kumaran'


class Solution:

    def absDiff(self, n1, n2):
        #print("dif",n1,n2)
        if n1 < n2:
            return  (n2-n1)
        else:
            return  (n1-n2)

    def twoSum(self, num, length, sumRequired):
        '''

        :param num: list
        :param length: length
        :return: list of pairs
        '''

        if length == 0:
            return  []

        bestDiff = None
        bestSum = None
        s = 0
        e = length-1
        while s < e:

            currSum = num[s] + num[e]
            if currSum == sumRequired:
                # can't get any closer
                bestSum = currSum
                break

            elif currSum < sumRequired:
                if bestDiff is None:
                    bestDiff = self.absDiff(sumRequired, currSum)
                    bestSum = currSum

                elif self.absDiff(sumRequired, currSum) < bestDiff:
                    bestDiff = self.absDiff(sumRequired, currSum)
                    bestSum = currSum

                # we need more to match sum
                # we have move the left cursor
                # skip duplicates
                #while s < length and [s] == num[s+1]:
                #    s += 1
                # move to next
                s += 1
            else:
                if bestDiff is None:
                    bestDiff = self.absDiff(sumRequired, currSum)
                    bestSum = currSum
                elif self.absDiff(sumRequired, currSum) < bestDiff:
                    bestDiff = self.absDiff(sumRequired, currSum)
                    bestSum = currSum
                # we need less to match sum
                # move right cursor
                # skip duplicates
                #while e > 0 and num[e] == num[e-1]:
                #    e -= 1
                # move to next
                e -= 1


        return bestSum






    def threeSumClosest(self, num, requiredSum):
        num = sorted(num)

        i = len(num)-1
        bestDif = None
        bestSum = None
        while i > 1:
            twoSum = self.twoSum(num, i, requiredSum-num[i])

            currSum = twoSum + num[i]

            if bestDif is None:
                bestDif = self.absDiff(requiredSum, currSum)
                bestSum = currSum

            elif self.absDiff(requiredSum, currSum) < bestDif:
                bestDif= self.absDiff(requiredSum, currSum)
                bestSum = currSum


            # move left with but, skip duplicates
            #while ( i > 2 and num[i-1] == num[i]):
            #    i -= 1
            i -= 1


        #print(output)
        return bestSum



if __name__ == '__main__':
    s = Solution()
    #print(s.threeSumClosest([0,2,1,-3], 1))

    print(s.threeSumClosest([1,1,-1,-1,3], 1))