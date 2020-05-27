# longest increasing seq

def lis(a):
    L = [0 for e in a]
    L[0] = 1
    for i in range (1, len(a)):
        for j in range(i):
            if a[j] < a[i] and L[j] > L[i]:
                L[i] = L[j]
        L[i] += 1
    print(L)
    return max(L)

def lis2(a):
    L = [[] for x in a]
    L[0] = [a[0]]

    for i in range(1, len(a)):
        for j in range(i):
            if a[j] < a[i] and len(L[j]) > len(L[i]):
                L[i] = L[j].copy()
        L[i].append(a[i])

    ret = L[0]
    for ll in L:
        if len(ll) > len(ret):
            ret = ll
    return ret

if __name__ == '__main__':
    A = [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]
    print("lis = ", lis2(A))
