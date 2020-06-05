def kadane(A):
    max_so_far = 0
    max_ending_here = 0
    for i in range(len(A)):
        max_ending_here = max_ending_here + A[i]
        max_ending_here = max(max_ending_here, 0)
        max_so_far = max(max_so_far, max_ending_here)
    return max_so_far

def kadaneCir(A):
    B = [-x for x in A]
    negMax = kadane(B)
    return max(kadane(A), sum(A) + negMax)


if __name__ == '__main__':
    A = [2, 1, -5, 4, -3, 1, -3, 4, -1]
    print("KadaneCir = ", kadaneCir(A))

