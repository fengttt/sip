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

if __name__ == '__main__':
    x = [random.randint(1, 100) for i in range(100)]
    ans = sorted(x)
    y = [i for i in x]
    qsortkr(y, 0, len(y))
    z = [i for i in x]
    qsort(z, 0, len(z) - 1) 

    print (z)
    print (y == ans)
    print (z == ans)

