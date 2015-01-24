faces = 6
dices = 3

sumT = 18

dpTable = []

# dpTable[dices][sum]

for i in range(dices + 1):
    dpTable.append([0] * (sumT + 1))

# base case with dice 1
for i in range(1, sumT + 1):
    if i <= faces:
        dpTable[1][i] = 1
    else:
        dpTable[1][i] = 0


def getSum2(d, s):

    for i in range(2, d+1):
        # possibles sums that can be achieved with i dices
        for j in range(i, min((s-(d-i)+1), i*faces+1)):
            #print(i,j,  min((s-(d-i)+1), i*faces+1))
            dpTable[i][j] = 0
            for k in range(1, faces+1):
                if j-k > 0:
                    dpTable[i][j] += dpTable[i-1][j-k]


getSum2(dices, sumT)

print([x for x in range(1, sumT+1)])
for i in range(1, dices + 1):
    print(dpTable[i][1:])


