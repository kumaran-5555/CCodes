import random




def bruteForce():
    sum1 = []
    sum2 = []

    s1 = 0
    s2 = 0

    for i in range(n):
        sum1.append(s1+r1[i])
        s1 += r1[i]

        sum2.append(s2+r2[i])
        s2 += r2[i]

    maxSum = sum1[n-1]
    maxLeft = -1
    maxRight = -1


    for i in range(n):
        for j in range(i,n):
            
            rightSum = sum1[n-1]-sum1[j]

            if i > 0:
                leftSum = sum1[i-1]
            else:
                leftSum = 0


            betweenSum = sum2[j]-sum2[i] + r2[i]


            if leftSum + rightSum + betweenSum > maxSum:
                maxSum = leftSum + rightSum + betweenSum
                maxLeft = i
                maxRight = j


    brute =  (maxSum, maxLeft, maxRight)
    return brute

def optimzed():

    sum1 = []
    sum2 = []

    s1 = 0
    s2 = 0

    for i in range(n):
        sum1.append(s1+r1[i])
        s1 += r1[i]

        sum2.append(s2+r2[i])
        s2 += r2[i]

    maxSum = sum1[n-1]
    maxLeft = -1
    maxRight = -1

    left = 0
    right = n-1

    while left <= right:

        while left < n and r1[left] > r2[left]:
            left += 1

        while right >= 0 and r1[right] >= r2[right]:
            right -= 1


        if left > right:
            break


        rightSum = sum1[n-1]-sum1[right]

        if left > 0:
            leftSum = sum1[left-1]
        else:
            leftSum = 0


        betweenSum = sum2[right]-sum2[left] + r2[left]


        if leftSum + rightSum + betweenSum > maxSum:
            maxSum = leftSum + rightSum + betweenSum
            maxLeft = left
            maxRight = right

        if left == right:
            # cant move
            break

        # decide where to move
        newLeft = min(left+1, right)

        while newLeft < right and r1[newLeft] >= r2[newLeft]:
            newLeft += 1

        newRight = max(right-1,left)

        while newRight > left and r1[newRight] >= r2[newRight]:
            newRight -= 1


        leftGain = sum1[newLeft-1] - sum1[left] + r1[left]
        leftLoss = sum2[newLeft-1] - sum2[left] + r2[left]
        leftBetween = sum2[right] - sum2[newLeft] + r2[newLeft]

        rightGain = sum1[right] - sum1[newRight+1] + r1[newRight+1]
        rightLoss = sum2[right] - sum2[newRight+1] + r2[newRight+1]
        rightBetween = sum2[newRight] - sum2[left] + r2[left]





        if leftGain + betweenSum -leftLoss < rightGain + betweenSum - rightLoss:
            right -= 1

        else:
            left += 1
    return (maxSum, maxLeft, maxRight)



def dpTry():
    inGap = 0
    gapYetTo = 1
    gapDone = 2

    dp = []

    for i in range(n):
        dp.append([0]*3)

    '''
    dp[i][inGap] = max value that we can get and we switched r2 and not yet back to r1
    dp[i][gapYetTo] = max value that we can get which we havenot yet switched to r2
    dp[i][gapDone] = max value that we can get after switching to r2 and back
    '''

    dp[0][inGap] = r2[0]
    dp[0][gapYetTo] = r1[0]
    dp[0][gapDone] = r1[0]

    

    for i in range(1,n):

        dp[i][inGap] = max(dp[i-1][inGap] + r2[i] , dp[i-1][gapYetTo] + r2[i])

        dp[i][gapYetTo] = dp[i-1][gapYetTo] + r1[i]
        dp[i][gapDone] = max(dp[i-1][inGap] + r1[i], dp[i-1][gapDone] + r1[i])


    return (max(dp[n-1][inGap], dp[n-1][gapYetTo], dp[n-1][gapDone]), 1, 1)






if __name__ == '__main__':

    for iterations in range(100):
        n = random.randint(1, 10)

        r1 = []
        r2 = []
   
        for i in range(n):

            r1.append(random.randint(1,100))
            r2.append(random.randint(1,100))


        brute = None
        print(r1, r2)

        brute = bruteForce()
        print(brute)

        
        optim = dpTry()

        # swap r1 and r2 to get another max


        print(brute, optim)
        assert(brute[0] == optim[0])



















