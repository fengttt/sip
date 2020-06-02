def findpath(M, i, j, cost, mem):
    if cost < 0:
        return 0

    if i == 0 and j == 0:
        if M[0][0] == cost:
            return 1
        else:
            return 0

    k = (i, j, cost)
    if k in mem:
        return mem[k]

    cnt = 0
    if i > 0:
        cnt += findpath(M, i-1, j, cost - M[i][j], mem)
    if j > 0:
        cnt += findpath(M, i, j-1, cost - M[i][j], mem)

    mem[k] = cnt
    return cnt

if __name__ == '__main__':
    M = [ [4,7,1,6],
            [5,7,3,9],
            [3,2,1,2],
            [7,1,6,3]]

    print ("Total paths of cost 25 = ", findpath(M, 3, 3, 25, {}))
