#!/usr/bin/python3

__doc__ = '''
8 queen problem, fifth edition 9.9
'''



def isValidMove(board, row, col, size):
	# check only rows above this
	
	# check for col intersect
	for i in range(0, row):
		if board[i][col] == 1:
			return False
	

	# check diagonal to top right
	j = row - 1
	for i in range(col+1, size):
		if j < 0:
			break
		if board[j][i] == 1:
			return False
		j-=1

	# check diagonal to top left
	j = row - 1
	for i in range(col-1, -1, -1):
		if j < 0:
			break
		if board[j][i] == 1:
			return False

		j-=1

	return True


def printBoard(board, size):

	print("---------solution-----------")
	for i in range(size):
		print(board[i])
	print("-----end solution-----------")


def queenProblem(board, currRow, size):
	if currRow == size:
		printBoard(board, size)
		return

	for i in range(0, size):
		if isValidMove(board, currRow, i, size):
			board[currRow][i] = 1
			queenProblem(board, currRow+1, size)
			board[currRow][i] = 0



if __name__== "__main__":
	board = []
	size = 11
	for i in range(size):
		board.append([0]*size)
	#printBoard(board, size)

	queenProblem(board, 0, size)

		
