def cc(S, n, N, lookup):
    if N == 0:
        return 1
    if n < 0 or N < 0:
        return 0
    k = (n, N)
    if k not in lookup:
        inc = cc(S, n, N-S[n], lookup)
        ex = cc(S, n-1, N, lookup)
        lookup[k] = inc + ex
    return lookup[k]

if __name__ == '__main__':
    S = [1, 2, 3]
    N = 4
    print("CC = ", cc(S, len(S)-1, 4, {}))
