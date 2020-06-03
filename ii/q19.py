def maxExpr(A):
    first = [float('-inf') for i in range(len(A) + 1)]
    second = [float('-inf') for i in range(len(A))]
    third = [float('-inf') for i in range(len(A) - 1)]
    fourth = [float('-inf') for i in range(len(A) - 2)]

    for i in reversed(range(len(A))):
        first[i] = max(first[i+1], A[i])

    for i in reversed(range(len(A) - 1)):
        second[i] = max(second[i+1], first[i] - A[i])

    for i in reversed(range(len(A) - 2)):
        third[i] = max(third[i+1], second[i] + A[i])

    for i in reversed(range(len(A) - 3)):
        fourth[i] = max(fourth[i+1], third[i] - A[i])

    return fourth[0]

if __name__ == '__main__':
    A = [3, 9, 10, 1, 30, 40]
    print ("Max expr = ", maxExpr(A))

