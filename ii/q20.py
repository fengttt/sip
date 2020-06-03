def subsetSum(A, n, s, mem):
    if s <= 0:
        return False

    if n == 0:
        return A[0] == s

    k = (n, s)
    if k in mem:
        return mem[k]

    res = subsetSum(A, n-1, s, mem) or subsetSum(A, n-1, s - A[n], mem)
    mem[k] = res
    return res

if __name__ == '__main__':
    A = [7, 3, 1, 5, 4, 8]
    s = sum(A)
    if s % 2 == 0:
        print("Can partition = ", subsetSum(A, len(A) - 1, s//2, {}))
    else:
        print("Sum is odd")


