def minCoins(S, N, mem):
    if N == 0:
        return 0
    if N not in mem:
        cnt = float('inf')
        for s in S:
            if s <= N:
                cnt = min(cnt, 1 + minCoins(S, N-s, mem))
        mem[N] = cnt
    return mem[N]

if __name__ == '__main__':
    S = [1, 3, 5, 7]
    print("Min Coin 15 = ", minCoins(S, 15, {}))
    print("Min Coin 18 = ", minCoins(S, 18, {}))
