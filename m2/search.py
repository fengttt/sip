import siplib.toy as toy

def showBoard(b):
    rows = ['Q.......',
            '.Q......',
            '..Q.....',
            '...Q....',
            '....Q...',
            '.....Q..',
            '......Q.',
            '.......Q']
    print(" ", "01234567")
    for i in range(8):
        print(i, rows[b[i]])

def checkValid(b): 
    for i in range(7):
        for j in range(i+1, 8):
            diff = b[i] - b[j]
            if diff == 0 or diff == i-j or diff == j-i:
                return False
    return True

if __name__ == '__main__':
    cnt = 0
    for r0 in range(8):
        for r1 in range(8):
            for r2 in range(8):
                for r3 in range(8):
                    for r4 in range(8):
                        for r5 in range(8):
                            for r6 in range(8):
                                for r7 in range(8):
                                    b = [r0, r1, r2, r3, r4, r5, r6, r7]
                                    if checkValid(b): 
                                        cnt += 1
                                        print("{0}-th solution: ".format(cnt))
                                        showBoard(b)

