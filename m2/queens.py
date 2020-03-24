import siplib.toy as toy

def showBoard(b):
    print(" ", "01234567")
    for i in range(8):
        print(i, b[i])

def checkPlace(b, x, y):
    for i in range(8):
        if b[y][i] == 'Q':
            return False
        if b[i][x] == 'Q':
            return False
        if x+i >= 0 and x+i < 8 and y+i >= 0 and y+i < 8 and b[y+i][x+i] == 'Q':
            return False
        if x-i >= 0 and x-i < 8 and y-i >= 0 and y-i < 8 and b[y-i][x-i] == 'Q':
            return False
        if x+i >= 0 and x+i < 8 and y-i >= 0 and y-i < 8 and b[y-i][x+i] == 'Q':
            return False
        if x-i >= 0 and x-i < 8 and y+i >= 0 and y+i < 8 and b[y+i][x-i] == 'Q':
            return False
    return True

if __name__ == '__main__':
    board = ['........' for i in range(8)]
    n = 0
    showBoard(board)
    while True:
        pos = input("Please place a Queen:\n")
        if pos == 'show':
            pass
        elif pos == 'hint':
            for y in range(8):
                for x in range(8):
                    if board[y][x] == '.' and not checkPlace(board, x, y):
                        board[y] = toy.writeCharAt(board[y], x, 'X')
        elif pos == '-hint':
            for y in range(8):
                for x in range(8):
                    if board[y][x] == 'X':
                        board[y] = toy.writeCharAt(board[y], x, '.')
        elif pos == 'reset':
            board = ['........' for i in range(8)]
            n = 0
        elif pos[0] == '-':
            x, y = int(pos[1]), int(pos[2])
            board[y] = toy.writeCharAt(board[y], x, '.')
            for y in range(8):
                for x in range(8):
                    if board[y][x] == 'X':
                        board[y] = toy.writeCharAt(board[y], x, '.')
        else:
            x, y = int(pos[0]), int(pos[1])
            if checkPlace(board, x, y):
                board[y] = toy.writeCharAt(board[y], x, 'Q')
                n += 1
            else:
                print("Invalid place.")
        showBoard(board)
        if n == 8:
            print("Good job!")
            break
