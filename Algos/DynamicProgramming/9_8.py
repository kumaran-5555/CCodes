#!/usr/bin/python3

__doc__ = '''

	no of ways of getting change,9.8, fifith edition
'''



def noOfWays(denomination, lenOfDenom, n):
	if n < 0:
		return 0
	if n == 0:
		return 1
	if lenOfDenom == 0:
		return 0
	return noOfWays(denomination, lenOfDenom-1, n) + noOfWays(denomination, lenOfDenom, n-denomination[lenOfDenom-1])





if __name__ == "__main__":
	print(noOfWays([1,2,3], 3, 4))
	print(noOfWays([2,5,3,6], 4, 10))
