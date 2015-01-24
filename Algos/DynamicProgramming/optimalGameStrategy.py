#!/usr/bin/python
__author__ = 'serajago'

# http://www.geeksforgeeks.org/dynamic-programming-set-31-optimal-strategy-for-a-game/
l = [20, 30, 2, 2, 2, 10]

player1First = []
player2First = []
player1Next = []
player2Next = []
N = len(l)
for i in range(N):
    player1First.append([0] * N)
    player2First.append([0] * N)
    player1Next.append([0] * N)
    player2Next.append([0] * N)

# trival if the list has only one element, whoever plays will win
for i in range(N):
    player1First[i][i] = l[i]
    player2First[i][i] = l[i]

# player1First[i][j] - holds the maximum that player1 can achieve from the game state l[i:j+1] and player1 plays first
# player1Next[i][j] - holds the maximum that player1 can achieve from the game state l[i:j+1] and player1 plays next


print("Player1First")
for i in range(N):
    print(player1First[i])

print("Player2First")

for i in range(N):
    print(player2First[i])

print("Player1Next")
for i in range(N):
    print(player1Next[i])

print("Player2Next")
for i in range(N):
    print(player2Next[i])


def getMaximum():
    for listSize in range(2, N + 1):
        i = 0
        while (i + listSize) <= N:
            # if player 1 playes he has two options
            # either choose from left or from right
            # player 1's total is
            # left's val + player1Next[left-1][right]
            left = i
            right = i + listSize - 1
            print(left, right)

            # player1First[left][right] = max(l[left] + player2First[left+1][right], l[right], player2First[left][right-1])
            player1First[left][right] = max(l[left] + player1Next[left + 1][right],
                                            l[right] + player1Next[left][right - 1])

            player2First[left][right] = max(l[left] + player2Next[left + 1][right],
                                            l[right] + player2Next[left][right - 1])


            if (l[left] + player1Next[left + 1][right]) > (l[right] + player1Next[left][right - 1]):
                player2Next[left][right] = player2First[left+1][right]
            else:
                player2Next[left][right] = player2First[left][right-1]

            if (l[left] + player2Next[left + 1][right]) > (l[right] + player2Next[left][right - 1]):
                player1Next[left][right] = player1First[left+1][right]
            else:
                player1Next[left][right] = player1First[left][right-1]
            i += 1
        #break


getMaximum()

print("Player1First")
for i in range(N):
    print(player1First[i])

print("Player2First")

for i in range(N):
    print(player2First[i])

print("Player1Next")
for i in range(N):
    print(player1Next[i])

print("Player2Next")
for i in range(N):
    print(player2Next[i])