import random

def exch(a, i, j):
    a[i], a[j] = a[j], a[i]

def qsortkr(a, lo, hi): 
    if lo >= hi:
        return

    mid = (lo + hi) // 2
    exch(a, lo, mid)
    last = lo
    for i in range(lo+1, hi):
        if a[i] < a[lo]:
            exch(a, last+1, i)
            last += 1
    exch(a, lo, last)
    qsortkr(a, lo, last)
    qsortkr(a, last+1, hi)

def partition(a, lo, hi):
    pivot = a[lo]
    i = lo
    j = hi + 1
    while True:
        i += 1
        while a[i] < pivot:
            if i == hi:
                break
            i += 1

        j -= 1
        while a[j] > pivot:
            j -= 1

        if i >= j:
            break
        exch(a, i, j)

    exch(a, lo, j)
    return j

def qsort(a, lo, hi):
    if lo >= hi:
        return
    j = partition(a, lo, hi)
    qsort(a, lo, j-1)
    qsort(a, j+1, hi)

def qsort2(a, lo, hi):
    if lo >= hi:
        return

    i = lo - 1
    j = hi
    v = a[hi]

    while True:
        while True:
            i = i+1
            if a[i] >= v:
                break
        while True:
            j = j-1
            if a[j] <= v or j == lo:
                break
        if i >= j:
            break
        exch(a, i, j)
    exch(a, i, hi)
    qsort2(a, lo, i-1)
    qsort2(a, i+1, hi)

def merge(a, b):
    i = 0
    j = 0
    ret = []

    while True:
        if i == len(a):
            ret.extend(b[j:])
            return ret
        elif j == len(b):
            ret.extend(a[i:])
            return ret
        elif a[i] < b[j]:
            ret.append(a[i])
            i += 1
        else:
            ret.append(b[j])
            j += 1
def msort(a): 
    if len(a) <= 1:
        return a.copy()

    mid = len(a) // 2

    b1 = msort(a[:mid])
    b2 = msort(a[mid:])
    return merge(b1, b2)

if __name__ == '__main__':
    x = [random.randint(1, 100) for i in range(100)]
    ans = sorted(x)
    y = [i for i in x]
    qsort(y, 0, len(y) - 1)
    z = [i for i in x]
    qsort2(z, 0, len(z) - 1)

    print (y == ans)
    print (z == ans)

