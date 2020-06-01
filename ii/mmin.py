def mmcost(M, i, j, mem):
    if i == 0 and j == 0:
        return M[0][0]

    c1 = float('inf')
    c2 = float('inf')

    if i > 0:
        c1 = mmcost(M, i-1, j, mem) 

    if j > 0: 
        c2 = mmcost(M, i, j-1, mem)

    c = min(c1, c2) + M[i][j]
    mem[(i, j)] = c
    return c

if __name__ == '__main__':
    cost = [    [4,7,8,6,4],
                [6,7,3,9,2],
                [3,8,1,2,4],
                [7,1,7,3,7],
                [2,9,8,9,3] ]

    print("Min cost = ", mmcost(cost, 4, 4, {})) 

