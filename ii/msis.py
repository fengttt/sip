# Increasing seq with max sum

def msis(a):
    s = [0 for x in a]
    s[0] = a[0]
    for i in range (1, len(a)):
        for j in range(i):
            if s[i] < s[j] and a[i] > a[j]:
                s[i] = s[j]
        s[i] += a[i]
    return max(s)

if __name__ == '__main__':
    a = [8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11]
    print ('msis = ', msis(a))
