# longest common subsequence.

def buildtbl(x, y, lenx, leny):
    t = [[0 for i in range(leny + 1)] for j in range(lenx + 1)]
    for i in range(lenx): 
        for j in range(leny): 
            if x[i] == y[j]:
                t[i+1][j+1] = t[i][j] + 1
            else:
                t[i+1][j+1] = max(t[i][j+1], t[i+1][j])
    return t

def onelcs(x, y, t, i, j):
    if i == 0 or j == 0:
        return ""
    if x[i-1] == y[j-1]:
        return onelcs(x, y, t, i-1, j-1) + x[i-1]
    if t[i-1][j] > t[i][j-1]:
        return onelcs(x, y, t, i-1, j)
    else:
        return onelcs(x, y, t, i, j-1)

def alllcs(x, y, t, i, j):
    if i == 0 or j == 0:
        return [""]
    if x[i-1] == y[j-1]:
        lcs = alllcs(x, y, t, i-1, j-1)
        return [s + x[i-1] for s in lcs]
    if t[i-1][j] > t[i][j-1]:
        return alllcs(x, y, t, i-1, j)
    elif t[i-1][j] < t[i][j-1]:
        return alllcs(x, y, t, i, j-1)
    else:
        return alllcs(x, y, t, i-1, j) + alllcs(x, y, t, i, j-1)

def alllcs_uniq(x, y, t):
    lenx = len(x)
    leny = len(y)
    arr = alllcs(x, y, t, lenx, leny)
    return set(arr)

if __name__ == '__main__':
    x = "ABCBDAB" 
    y = "BDCABA"

    lenx = len(x)
    leny = len(y)
    t = buildtbl(x, y, lenx, leny)

    print("LCS len = ", t[-1][-1])
    print("One lcs = ", onelcs(x, y, t, lenx, leny))
    print("All lcs = ", alllcs_uniq(x, y, t))
