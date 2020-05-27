# longest common substr in x[0:m], y[0:n]
def lcsub(x, y, m, n):
    maxlen = 0
    endingx = m
    endingy = n

    t = [[0 for j in range(n+1)] for i in range(m+1)]
    for i in range(m):
        for j in range(n):
            if x[i] == y[j]:
                t[i+1][j+1] = t[i][j] + 1
                if t[i+1][j+1] > maxlen:
                    maxlen = t[i+1][j+1]
                    endingx, endingy = i, j
    return maxlen, endingx, endingy

if __name__ == '__main__':
    X = "ABC"
    Y = "BABA"

    sz, x, y = lcsub(X, Y, len(X), len(Y))
    print("LCS: ", sz, x, y, "x:", X[x+1-sz:x+1], "y:", Y[y+1-sz:y+1])

