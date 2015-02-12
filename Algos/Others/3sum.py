__author__ = 'kumaran'


class Solution:
    def twoSum(self, num, length, sumRequired):
        '''

        :param num: list
        :param length: length
        :return: list of pairs
        '''

        if length == 0:
            return  []

        output = []
        s = 0
        e = length-1
        while s < e:
            if num[s] + num[e] == sumRequired:
                output.append([num[s],num[e]])
                # move both
                # skip duplicates
                while s < length and [s] == num[s+1]:
                    s += 1
                # move to next
                s += 1

                while e > 0 and num[e] == num[e-1]:
                    e -= 1
                # move to next
                e -= 1

            elif num[s] + num[e] < sumRequired:
                # we need more to match sum
                # we have move the left cursor
                # skip duplicates
                while s < length and [s] == num[s+1]:
                    s += 1
                # move to next
                s += 1
            else:
                # we need less to match sum
                # move right cursor
                # skip duplicates
                while e > 0 and num[e] == num[e-1]:
                    e -= 1
                # move to next
                e -= 1

        #print(num, length, sumRequired, output)
        return output






    def threeSum(self, num):
        output = []
        num = sorted(num)

        i = len(num)-1

        while i > 1:
            sum2Ouput = self.twoSum(num, i, -num[i])
            if len(sum2Ouput):
                for t in sum2Ouput:
                    t.append(num[i])
                    output.append(t)
            # move left with but, skip duplicates
            while ( i > 2 and num[i-1] == num[i]):
                i -= 1
            i -= 1


        #print(output)
        return output


