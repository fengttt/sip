def seq(M, i, j, mem):
    if (i, j) in mem:
        return mem[(i, j)]

    s = 1 
    if i > 0 and M[i][j] + 1 == M[i-1][j]:
        ss = 1 + seq(M, i-1, j, mem)
        s = max(s, ss)
    if j > 0 and M[i][j] + 1 == M[i][j-1]:
        ss = 1 + seq(M, i, j-1, mem)
        s = max(s, ss)
    if i < len(M) -1 and M[i][j] + 1 == M[i+1][j]:
        ss = 1 + seq(M, i+1, j, mem)
        s = max(s, ss)
    if j < len(M[0]) -1 and M[i][j] + 1 == M[i][j+1]:
        ss = 1 + seq(M, i, j+1, mem)
        s = max(s, ss)

    mem[(i, j)] = s
    return s

def findseq(M):
    ss = 0
    mem = {}
    for i in range(len(M)):
        for j in range(len(M[0])):
            s = seq(M, i, j, mem)
            ss = max(s, ss)
    return ss

if __name__ == '__main__':
    m = [[10,13,14,21,23],
            [11,9,22,2,3],
            [12,8,1,5,4],
            [15,24,7,6,20],
            [16,17,18,19,26]]

    print("Long seq = ", findseq(m))
