def showBoard(b):
    print(" ", "012")
    for y in range(3):
        print(y, "".join((b[0][y], b[1][y], b[2][y])))

def checkWinner(b, c):
    for i in range(3):
        if b[i][0] == c and b[i][1] == c and b[i][2] == c:
            return True
        if b[0][i] == c and b[1][i] == c and b[2][i] == c:
            return True
    if b[0][0] == c and b[1][1] == c and b[2][2] == c:
        return True
    if b[2][0] == c and b[1][1] == c and b[0][2] == c:
        return True
    return False

def checkEnd(b):
    for i in range(3):
        for j in range(3):
            if b[i][j] == '.':
                return False
    return True

if __name__ == '__main__':
    board = [['.', '.', '.'] for i in range(3)] 
    showBoard(board)
    while True:
        pos = input("Please place a piece:\n")
        if pos == 'reset':
            board = [['.', '.', '.'] for i in range(3)] 
        elif pos[0] == 'x' or pos[0] == 'o':
            x, y = int(pos[1]), int(pos[2])
            if board[x][y] == '.':
                board[x][y] = pos[0] 
                if checkWinner(board, pos[0]):
                    showBoard(board)
                    print(pos[0], "won the game.")
                    break
            else:
                print("Invalid move.")
        else:
            print(pos, "is not a valid move.")
        showBoard(board)
        if checkEnd(board):
            print("End of Game")
            break
