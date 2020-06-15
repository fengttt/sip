def maxsum(A, n, mem):
    if n < 0: 
        return 0

    if n not in mem:
        inc = A[n] + maxsum(A, n-2, mem)
        ex = maxsum(A, n-1, mem)
        mem[n] = max(inc, ex)

    return mem[n]

if __name__ == '__main__':
    A = [1, 2, 9, 4, 5, 0, 4, 11, 6]
    print("Max = ", maxsum(A, len(A)-1, {}))


