def cutRod(n):
    t = [i for i in range(n+1)]
    for i in range(2, n+1):
        for j in range(1, i):
            t[i] = max(t[i], j * t[i-j])

    return t[n]

def cutRodMem(n, mem):
    if n <= 1:
        return n

    if n not in mem:
        best = n
        for i in range(1, n):
            best = max(best, i * cutRodMem(n-i, mem))
        mem[n] = best
    return mem[n]

if __name__ == '__main__':
    print("Cut rod 100 = ", cutRod(100))
    print("Cut rod 100 = ", cutRodMem(100, {}))
