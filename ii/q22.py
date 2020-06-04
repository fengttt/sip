def minPart(S, n, S1, S2, mem):
    if n < 0:
        return abs(S1 - S2)

    k = (n, S1)
    if k not in mem:
        inc = minPart(S, n-1, S1+S[n], S2, mem)
        exc = minPart(S, n-1, S1, S2+S[n], mem)
        mem[k] = min(inc, exc)
    return mem[k]

if __name__ == '__main__':
    S = [10, 20, 15, 5, 25]
    print ("Min diff part = ", minPart(S, 4, 0, 0, {}))
