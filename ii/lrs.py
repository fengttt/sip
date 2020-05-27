# longest repeating subsequence.

def lrs(x, m, n):
    if m == 0 or n == 0:
        return 0
    if x[m-1] == x[n-1] and m!=n:
        return lrs(x, m-1, n-1) + 1
    return max(lrs(x, m-1, n), lrs(x, m, n-1))

def lkuplrs(x, m, n, lookup):
    if m == 0 or n == 0:
        return 0

    # if m > n:
    #    return lkuplrs(x, n, m, lookup)

    if (m, n) not in lookup:
        if x[m-1] == x[n-1] and m!=n:
            lookup[(m, n)] = lkuplrs(x, m-1, n-1, lookup) + 1
        else:
            lookup[(m, n)] = max(
                    lkuplrs(x, m-1, n, lookup),
                    lkuplrs(x, m, n-1, lookup)
                    )

    return lookup[(m, n)]

def btuplrs(x):
    n = len(x)
    t = [[0 for i in range(n+1)] for j in range(n+1)]
    for i in range(1, n+1):
        for j in range(1, n+1):
            if x[i-1] == x[j-1] and i != j:
                t[i][j] = t[i-1][j-1] + 1
            else:
                t[i][j] = max(t[i-1][j], t[i][j-1])
    # for i in range(n+1):
    #    print(t[i])
    return t[n][n]




if __name__ == '__main__':
    X = "ATACTCGGAACTTCAGCATTCAACGGACTCAGAAGAAA"
    # print("LRS = ", lrs(X, len(X), len(X)))
    lookup = {}
    print("LRS = ", lkuplrs(X, len(X), len(X), lookup))
    print("LRS = ", btuplrs(X)) 

