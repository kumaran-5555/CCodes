#!/usr/bin/python3
__author__ = 'kumaran'

#http://www.careercup.com/question?id=5739192933941248


class Solution():
    def calenderIntervals(self, person1, person2):
        '''

        :param person1: list of busy times even indicies are start, odd indices are end
        :param person2: list of busy times even indicies are start, odd indices are end
        :return: list of free intervals

        do a line sweep
        '''

        l1 = len(person1)
        l2 = len(person2)

        i = 0
        j = 0
        output = []
        iSPerson1Busy = False
        isPerson2Busy = False
        while i < l1  and j < l2:
            print(i,j,person1[i], person2[j], iSPerson1Busy, isPerson2Busy)
            if person1[i] < person2[j]:

                if i%2 == 0:

                    # starting time for person1
                    # ending of the free time
                    if not isPerson2Busy and not iSPerson1Busy:
                        output.append(person1[i]-1)

                    iSPerson1Busy = True


                else:
                    iSPerson1Busy = False

                    # ending time for person1
                    # starting of free time
                    if not isPerson2Busy:
                        output.append(person1[i]+1)


                i += 1
            elif person1[i] > person2[j]:
                # person 2's time
                if j%2 == 0:
                    # starting time for person2
                    if not isPerson2Busy and not iSPerson1Busy:
                        output.append(person2[j]-1)
                    isPerson2Busy = True
                else:
                    isPerson2Busy = False
                    # ending time for person2
                    if not iSPerson1Busy:
                        output.append(person2[j]+1)
                j += 1
            else:
                # can not get any output in this interval
                if i%2 == 0:
                    # starting time of person1
                    iSPerson1Busy = True
                    i += 1
                else:
                    # ending time for person1
                    iSPerson1Busy = False
                    i += 1

                if j%2 == 0:
                    isPerson2Busy = True
                    j += 1
                else:
                    isPerson2Busy = False
                    j += 1

                if not isPerson2Busy and not iSPerson1Busy:
                    # starting of free time
                    output.append(person2[j-1]+1)

                elif isPerson2Busy and iSPerson1Busy:
                    output.append(person2[j-1]-1)

        # only person1 has things, whenever he/she is free,we are good
        while i < l1:
            if i%2 == 0:
                output.append(person1[i]-1)
            else:
                output.append(person1[i]+1)
            i += 1

        while j < l2:
            if i%2 == 0:
                 output.append(person2[j]-1)
            else:
                output.append(person2[j]+1)
            j += 1

        output = output[1:-1]

        return output


    def _interleave(self, s1, s2, s3,d):

        key = "%d-%d-%d"%(len(s1),len(s2), len(s3))

        if key in d:
            return d[key]

        #print(len(s1),len(s2),len(s3))
        if not len(s3) and not len(s1) and not len(s2):
            d[key] = True
            return True

        if not len(s3):
            d[key] = False
            return False

        if len(s1) and len(s2) and s3[0] == s1[0] and s3[0] == s1[0]:
            # try to consume from s1 and if it works out
            if self._interleave(s1[1:], s2[:], s3[1:],d):
                d[key] = True
                return True
            elif self._interleave(s1[:], s2[1:], s3[1:],d):
                d[key] = True
                return True
        elif len(s1) and s3[0] == s1[0]:
            # try to consume from s1 and if it works out
            if self._interleave(s1[1:], s2[:], s3[1:],d):
                d[key] = True
                return True
        elif len(s2) and s3[0] == s2[0]:
            # try to consume from s2 and if it works out
            if self._interleave(s1[:], s2[1:], s3[1:],d):
                d[key] = True
                return True
        else:
            d[key] = False
            return False

        d[key] = False
        return False


    # @return a boolean
    def isInterleave(self, s1, s2, s3):
        print(self._interleave(s1,s2,s3,{}))











if __name__ == '__main__':
    s = Solution()
    #print(s.calenderIntervals([1,5,10,14,19,20,21,24,27,30],[3,5,12,15,18,21,23,24]))
    #print(s.calenderIntervals([1,5,10,15],[6,10,15,20]))
    s.isInterleave("aabcc", "dbbca","aadbbcbcac")
    #s.isInterleave("bbbbbabbbbabaababaaaabbababbaaabbabbaaabaaaaababbbababbbbbabbbbababbabaabababbbaabababababbbaaababaa", "babaaaabbababbbabbbbaabaabbaabbbbaabaaabaababaaaabaaabbaaabaaaabaabaabbbbbbbbbbbabaaabbababbabbabaab", "babbbabbbaaabbababbbbababaabbabaabaaabbbbabbbaaabbbaaaaabbbbaabbaaabababbaaaaaabababbababaababbababbbababbbbaaaabaabbabbaaaaabbabbaaaabbbaabaaabaababaababbaaabbbbbabbbbaabbabaabbbbabaaabbababbabbabbab")