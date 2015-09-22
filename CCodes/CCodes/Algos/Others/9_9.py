#!/usr/bin/python3

__doc__ = '''
8 queen problem, fifth edition 9.9
'''



def isValidMove(board, row, col, size):
	# check only rows above this
	
	# check for col intersect
	for i in range(0, row):
		if board[i][col] == 'Q':
			return False
	

	# check diagonal to top right
	j = row - 1
	for i in range(col+1, size):
		if j < 0:
			break
		if board[j][i] == 'Q':
			return False
		j-=1

	# check diagonal to top left
	j = row - 1
	for i in range(col-1, -1, -1):
		if j < 0:
			break
		if board[j][i] == 'Q':
			return False

		j-=1

	return True


def printBoard(board, size):
	pass

	print("---------solution-----------")
	for i in range(size):
		print(board[i])
	print("-----end solution-----------")


def queenProblem(board, currRow, size, output):
	if currRow == size:
		printBoard(board, size)
		output.append(board[:])
		return

	for i in range(0, size):
		if isValidMove(board, currRow, i, size):
			board[currRow][i] = 'Q'
			queenProblem(board, currRow+1, size, output)
			board[currRow][i] = '.'



if __name__== "__main__":
	board = []
	size = 4
	for i in range(size):
		board.append(['.']*size)
	#printBoard(board, size)

	output = []
	queenProblem(board, 0, size, output)
	print(output)

		
