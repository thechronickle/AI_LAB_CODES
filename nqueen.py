global N
N = int(input("Enter the No of Queens :"))
Board = [['_' for i in range(N)] for x in range(N)]
print(Board)


def isSafe(chessBoard, i, j):
    for row in range(len(chessBoard)):
        for col in range(len(chessBoard[i])):
            if chessBoard[row][col] == 'Q':
                jDist = abs(j - col)
                iDist = abs(i - row)
                if i == row or j == col or iDist == jDist:
                    return False
    return True


def printBoard(chessBoard):
    for i in chessBoard:
        for j in i:
            print(j, end="")
        print("")


def SolveQueen(Board, col):
    if col >= N:
        return True
    for i in range(N):
        if isSafe(Board, i,col):
            Board[i][col] = 'Q'
            printBoard(Board)
            print(" ")
            if SolveQueen(Board, col + 1):
                return True
            Board[i][col] = "_"
    return False


if SolveQueen(Board, 0) == False:
    print('\nSolution not exist')
else:
    print('\nFinal solution')
    printBoard(Board)