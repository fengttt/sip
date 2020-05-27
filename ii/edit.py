def dist(x, y): 
    m, n = len(x), len(y)
    t = [[0 for j in range(n+1)] for i in range(m+1)]

    for i in range(1, m+1):
        t[i][0] = i
    for j in range(1, n+1):
        t[0][j] = j

    for i in range(1, m+1):
        for j in range(1, n+1):
            if x[i-1] == y[j-1]:
                cost = 0
            else:
                cost = 1
            t[i][j] = min(t[i-1][j] + 1,
                          t[i][j-1] + 1,
                          t[i-1][j-1] + cost)
    return t[m][n]


if __name__ == '__main__':
    x = 'kitten'
    y = 'sitting'
    print(" dist =", dist(x, y))



