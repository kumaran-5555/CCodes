__author__ = 'serajago'

class BichromeBoard:
    def ableToDraw(self, board):
        # consider even,even indices as white
        # check if board matches
        r = len(board)
        c = len(board[0])
        isPossible=True
        for i in range(r):
            for j in range(c):
                if i%2 == 0 and j%2 == 0 and board[i][j] == 'B':
                    isPossible = False
                elif board[i][j] == 'W':
                    isPossible = False

        if isPossible:
            return "Possible"

        isPossible = True
        # consider even,even indices as black
        for i in range(r):
            for j in range(c):
                if i%2 == 0 and j%2 == 0 and board[i][j] == 'W':
                    isPossible = False
                elif board[i][j] == 'B':
                    isPossible = False

        if isPossible:
            return "Possible"

        return "Impossible"





if __name__ == '__main__':
    s = BichromeBoard()
    print(s.ableToDraw(["W??W"]))