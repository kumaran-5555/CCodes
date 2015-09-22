__author__ = 'serajago'


# http://www.geeksforgeeks.org/dynamic-programming-subset-sum-problem/

l = [3, 34, 4, 12, 5, 2]
sum = 34

dpTable = []
for i in range(len(l)):
    dpTable.append([False] * (sum + 1))


# dpTable[i][j] = True if l[:i+1] has a subset with sum j

# dpTable[i][j] = True if l[:i] has subset with sum j or l[:i] has subset with sum j-l[i]
# dpTable[i][j] = True if dpTable[i-1][j] or dpTable[i-1][j-l[i]]


def subsetSum():
    # base case
    for s in range(0, sum + 1):
        if s == l[0]:
            dpTable[0][s] = True
        dpTable[0][0] = True

    for i in range(1, len(l)):
        for s in range(0, sum + 1):
            dpTable[i][s] = dpTable[i-1][s] or (dpTable[i-1][s-l[i]] if (s-l[i] >= 0) else False)





subsetSum()

for i in range(len(l)):
    print(dpTable[i])



