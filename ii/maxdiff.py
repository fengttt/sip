def maxdiff(a):
    minsofar = a[0]
    sofar = a[0]
    for i in range(1, len(a)):
        if a[i] < minsofar:
            minsofar = a[i]
        sofar = max(sofar, a[i] - minsofar)
    return sofar

if __name__ == '__main__':
    a = [2, 7, 9, 5, 1, 3, 9, 5]
    print("Maxdiff = ", maxdiff(a))

