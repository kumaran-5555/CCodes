#!/usr/bin/python
__author__ = 'serajago'

# http://www.geeksforgeeks.org/dynamic-programming-set-32-word-break-problem/

words = ["i", "like", "sam", "sung", "samsung", "mobile", "ice",
         "cream", "icecream", "man", "go", "mango"]

currIndex = [0] * len(words)
str = "ilikesamsungsam"

dpTable = []

for i in words:
    dpTable.append([0] * len(str))

for i in range(0, len(str)):
    for j in range(0, len(words)):
        if len(words[j]) > currIndex[j]:
            if words[j][currIndex[j]] == str[i]:
                currIndex[j] += 1
                dpTable[j][i] = 1
            else:
                currIndex[j] = 0
            if currIndex[j] == len(words[j]):
                currIndex[j] = 0
for i in range(0, len(words)):
    print(dpTable[i],"\t",words[i], currIndex[i])
