# find the lastest square of 1s.

def findsq1(M, m, n, sofar):
    if m == 0 or n == 0:
        return M[m][n], max(M[m][n], sofar)

    left, sofar = findsq1(M, m, n-1, sofar)
    top, sofar = findsq1(M, m-1, n, sofar)
    lefttop, sofar = findsq1(M, m-1, n-1, sofar)

    if M[m][n] == 0:
        sz = 0
    else:
        sz = 1 + min(left, top, lefttop)
    return sz, max(sofar, sz)

if __name__ == '__main__':
    M = [
        [0, 0, 1, 0, 1, 1],
        [0, 0, 1, 0, 1, 1],
        [0, 0, 1, 1, 1, 1],
        [0, 0, 1, 1, 1, 0],
        [0, 0, 1, 1, 1, 1],
        [0, 0, 1, 1, 1, 1],
        [0, 0, 1, 0, 1, 1],
        [0, 0, 1, 1, 1, 1],
        [0, 0, 1, 0, 1, 1],
    ]

    print("Max sq1 = ", findsq1(M, len(M) - 1, len(M[0]) - 1, 0))
