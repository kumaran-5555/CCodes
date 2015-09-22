#!/usr/bin/python
__author__ = 'serajago'

# http://www.geeksforgeeks.org/count-number-binary-strings-without-consecutive-1s/
N = 11

endingWithZero = [0] * (N+1)
endingWithOne = [0] * (N+1)

# for every new i position, number of strings having non-subsequents 1's are
# numberOfStrings of i-1 length ending with zero + numberOfString of i-1 length ending with one
# +
# numberOfString of i-1 length ending with zero

endingWithOne[1] = 1
endingWithZero[1] = 1

for i in range(2, N + 1):
    endingWithOne[i] = endingWithZero[i - 1]
    endingWithZero[i] = endingWithOne[i - 1] + endingWithZero[i-1]

print(endingWithZero[:N])
print(endingWithOne[:N])
