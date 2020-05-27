# longest increasing seq

def lis(a):
    L = [0 for e in a]
    L[0] = 1
    for i in range (1, len(a)):
        for j in range(i):
            if a[j] < a[i] and L[j] > L[i]:
                L[i] = L[j]
        L[i] += 1
    return L

def lis2(a):
    L = [[] for x in a]
    L[0] = [a[0]]

    for i in range(1, len(a)):
        for j in range(i):
            if a[j] < a[i] and len(L[j]) > len(L[i]):
                L[i] = L[j].copy()
        L[i].append(a[i])
    return L[-1]

if __name__ == '__main__':
    A = [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]
    lr = lis(A)
    rl = list(reversed(lis(list(reversed(A)))))
    lbs = [lr[i] + rl[i] - 1 for i in range(len(A))]
    print("  A = ", A)
    print(" lr = ", lr)
    print(" rl = ", rl)
    print("lbs = ", lbs)
