# build lcs length table.
def lcstab(x, y):
    t = [[0 for j in range(len(y) + 1)] for i in range(len(x) + 1)]
    for i in range(1, len(x) + 1):
        for j in range(1, len(y) + 1):
            if x[i-1] == y[j-1]:
                t[i][j] = t[i-1][j-1] + 1
            else:
                t[i][j] = max(t[i-1][j], t[i][j-1])
    return t

def diff(x, y, t):
    result = ''
    i, j = len(x), len(y)
    while i > 0 or j > 0:
        if i > 0 and t[i-1][j] == t[i][j]:
            result = ' -' + x[i - 1] + result
            i-=1
        elif j > 0 and t[i][j-1] == t[i][j]:
            result = ' +' + y[j - 1] + result
            j-=1
        else:
            result = ' ' + x[i-1] + result
            i-=1
            j-=1
    return result

if __name__ == '__main__':
    X = "ABCDFGHJQZ"
    Y = "ABCDEFGIJKRXYZ"

    t = lcstab(X, Y)
    d = diff(X, Y, t)
    print("Diff = ", d)


