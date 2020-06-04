def dp(n):
    t = [[0, 0] for x in range(n+1)]
    t[1][0] = 2
    t[1][1] = 1

    for i in range(2, n+1):
        t[i][0] = t[i-1][0] + t[i-1][1]
        t[i][1] = t[i-1][0]

    return t[n][0]

if __name__ == '__main__':
    print("cnt = ", dp(5))
