__author__ = 'serajago'

__author__ = 'serajago'
__author__ = 'serajago'

l = [10, 22, 9, 33, 21, 50, 41, 60, 80]

def LongestIncreasingSubseq(l):
    n = len(l)
    dpTable = [0] * (n + 1)
    print(type(dpTable))
    # LIS[j] holds the value of LIS in list[:j]
    # val[j] holds the last element of LIS in list[:j]

    # lis[j] = max( lis[i] where list[i] < list[j] and i < j) + 1

    # lis[0] is 0
    dpTable[0] = 0
    dpTable[1] = 1


    for i in range(2, n + 1):
        maxLen = 0
        for j in range(1, i):
            if l[j-1] < l[i-1]:
                maxLen = max(dpTable[j] + 1, maxLen)
        dpTable[i] = maxLen

#LongestIncreasingSubseq(l)


def lis(array):
    'Return one of the L.I.S. of list array'
    l = []
    for i in range(len(array)):
        # get the previous max-LIS list
        x = [l[j] for j in range(i) if l[j][-1] < array[i]] or [[]]
        print(l)
        jMaxList = max(x, key=len)
        l.append(jMaxList + [array[i]])
    lisSeq = max(l, key=len)
    print(l)
    return lisSeq, len(lisSeq)


def main():
    seq = [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]

    lisSeq, lisSeqLength = lis(seq)
    print  (   "\n" + "length of LIS = " + str(lisSeqLength) + "\n")
    print(    "\n" + "LIS sequence = " + str(lisSeq) + "\n")

if __name__ == "__main__":
    main()



