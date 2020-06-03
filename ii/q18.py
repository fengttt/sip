def knapsack(v, w, N, W, mem):
    if W < 0:
        return float('-inf')
    if N < 0 or W == 0:
        return 0
    k = (N, W)
    if k not in mem:
        inc = v[N] + knapsack(v, w, N-1, W-w[N], mem)
        exc = knapsack(v, w, N-1, W, mem)
        mem[k] = max(inc, exc)
    return mem[k]

if __name__ == '__main__':
    v = [20, 5, 10, 40, 15, 25]
    w = [1, 2, 3, 8, 7, 4]
    print("Knapsack with w 10 = ", knapsack(v, w, 5, 10, {}))
