def mcmp(dims, i, j, m):
    if j <= i + 1:
        return 0

    mincost = float('inf')
    if m[i][j] == 0:
        for k in range(i+1, j):
            cost = mcmp(dims, i, k, m)
            cost += mcmp(dims, k, j, m)
            cost += dims[i] * dims[k] * dims[j]
            if cost < mincost:
                mincost = cost
        m[i][j] = mincost
    return m[i][j]

if __name__ == '__main__':
    dims = [10, 30, 5, 60]
    m = [[0 for x in range(len(dims))] for y in range(len(dims))]
    print ("Min cost = ", mcmp(dims, 0, len(dims)-1, m))
