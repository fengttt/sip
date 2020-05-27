# length of longest palindromic subseq
def palinLen(x, i, j):
    if i > j:
        return 0
    if i == j:
        return 1
    if x[i] == x[j]:
        return palinLen(x, i+1, j-1) + 2
    else:
        return max(palinLen(x, i+1, j), palinLen(x, i, j-1))

def dynPalinLen(x):
    lx = len(x)
    t = [[0 for i in range(lx+1)] for j in range(lx+1)]

    for sz in range(1, lx+1):
        for i in range(lx-sz+1):
            if sz == 1:
                t[i][i+1] = 1
            elif x[i] == x[i+sz-1]:
                t[i][i+sz] = t[i+1][i+sz-1] + 2
            else:
                t[i][i+sz] = max(t[i+1][i+sz], t[i][i+sz-1])

    # for i in range(lx+1):
    #    print(t[i])

    return t[0][lx]


if __name__ == '__main__':
    X = "ABBDCdafa3adfa3r414334143darerfqfeeqvfqr45rdedareq1254t5eeeeq33qaQQERQRqAACB"
    # X = "ABBDCAACB"
    # print ("Max palin len = ", palinLen(X, 0, len(X) - 1))
    print ("Max palin len = ", dynPalinLen(X)) 

