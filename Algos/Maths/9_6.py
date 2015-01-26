#!/usr/bin/python3

__doc__ = '''

9.6 fifth edition printing matching paranthesis
'''


def printMatching(strOut, noStarting, noEnding, currPosition):

	#print(strOut, noStarting, noEnding, currPosition)
	
	if not noStarting and not noEnding:
		print("".join(strOut))
		return
	
	if noEnding > noStarting:
		strOut[currPosition] = '}'
		printMatching(strOut, noStarting, noEnding-1, currPosition+1)

	if noStarting > 0:
		strOut[currPosition] = '{'
		printMatching(strOut, noStarting-1, noEnding, currPosition+1)

	



if __name__ == '__main__':
	size = 3
	strOut = [None] * size * 2
	printMatching(strOut, size, size, 0)


