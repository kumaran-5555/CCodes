#!/usr/bin/python

# http://en.wikipedia.org/wiki/Permutation

def generate_permutation(listOfAlphabets):
    # create a lowest permutation
    l = sorted(listOfAlphabets)
    output = []

    output.append("".join(l))

    while True:

        # find largest k such that l[k]<l[k+1], is no k, terminate
        k = -1
        for i in range(len(l) - 1):
            if l[i] < l[i + 1]:
                k = i
        if k == -1:
            return  output
            return
        # find largest i such that l[k] < l[i]
        for i in range(k + 1, len(l)):
            if l[k] < l[i]:
                j = i

        # print(k,j,l[k],l[j])
        # swap l[k] and l[i]
        temp = l[k]
        l[k] = l[j]
        l[j] = temp

        # revert l[k+1:]
        i = k + 1
        j = len(l) - 1
        while i < j:
            temp = l[i]
            l[i] = l[j]
            l[j] = temp
            i += 1
            j -= 1
        output.append("".join(l))

    return output

class Solution:
    # @param num, a list of integer
    # @return a list of lists of integers
    def permute(self, num):
        output = []
        sortedNum = sorted(num)
        l = len(num)
        output.append(sortedNum[:])

        while True:
            k = None
            for i in range(l-1):
                if sortedNum[i] < sortedNum[i+1]:
                    k = i
            if k is None:
                # we are done
                break

            # find largest m such that sortedNum[k] < sortedNum[m]
            for i in range(k+1,l):
                if sortedNum[k] < sortedNum[i]:
                    m = i

            # swap k and m
            temp = sortedNum[k]
            sortedNum[k] = sortedNum[m]
            sortedNum[m] = temp

            # revesr sortedNum[k+1:]
            sortedNum = sortedNum[:k+1] + sorted(sortedNum[k+1:], reverse=False)

            output.append(sortedNum[:])

        return output



if __name__ == "__main__":
    #print(generate_permutation(['foo', 'bar', 'hhh', 'aaa']))
    s = Solution()
    print(s.permute([1,1,2]))

