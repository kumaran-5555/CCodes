__author__ = 'serajago'

# http://www.geeksforgeeks.org/length-of-the-longest-arithmatic-progression-in-a-sorted-array/

l = {1, 7, 10, 15, 27, 29}
N = len(l)
arithmeticDelta = [0] * N
count = [0] * N
lastMember = [0] * N

arithmeticDelta[0] = 0
count[0] = 1
lastMember[0] = l[0]
for i in range(0, N):




