def rodCut(p, n):
    profits = [0 for i in range(n+1)]
    for i in range(1, n+1):
        prof = 0
        for j in range(0, i):
            pj = p[j] + profits[i-j-1]
            prof = max(prof, pj)
        profits[i] = prof
    return profits[n]

if __name__ == '__main__':
    prices = [1, 5, 8, 9, 10, 17, 17, 20]
    print ('Profit of rod 4 = ', rodCut(prices, 4))
