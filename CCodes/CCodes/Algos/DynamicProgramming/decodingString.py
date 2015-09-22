__author__ = 'serajago'
# http://www.geeksforgeeks.org/count-possible-decodings-given-digit-sequence/

str = "120"

strLen = len(str)

dpTable = [0] * (strLen + 1)
# dpTable[i] holds the total number of decodings of str[:i]
# update rules
# if (int(str[i-1:i-1+2]) <= 26)
# dpTable[i] =  dpTable[i-1] + 2
# else
# dpTable[i] = dpTable[i-1] + 1

dpTable[0] = 0
dpTable[1] = 1
for i in range(2, strLen + 1):
    lastTwoPosition = 0
    lastButOnePosition = 0
    onlyLastPosition = 0
    print(i, str[i - 2:i - 2 + 2], str[i-1], dpTable)
    lastTwo = int(str[i - 2:i - 2 + 2])
    lastOne = int(str[i - 1])
    if lastTwo <= 26 and lastTwo > 9:
        if lastOne > 0:
            lastTwoPosition = dpTable[i-2] + 2
        else:
            lastButOnePosition = dpTable[i-2]
    elif lastOne > 0:
        onlyLastPosition = dpTable[i-1]

    print(lastTwoPosition, lastButOnePosition, onlyLastPosition)
    dpTable[i] = max(max(lastButOnePosition, lastTwoPosition), onlyLastPosition)
    print(i, str[i - 2:i - 2 + 2], dpTable)

print(dpTable)




