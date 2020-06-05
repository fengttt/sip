def cnt(X, Y, m, n, mem):
    if n == 0:
        return 1

    if m < n:
        return 0

    k = (m, n)
    res = 0
    if k not in mem:
        if X[m-1] == Y[n-1]:
            res = cnt(X, Y, m-1, n-1, mem) + cnt(X, Y, m-1, n, mem)
        else:
            res = cnt(X, Y, m-1, n, mem)

        mem[k] = res
    return mem[k]

if __name__ == '__main__':
    X = 'subsequence'
    Y = 'sue'
    print("Cnt = ", cnt(X, Y, len(X), len(Y), {}))
