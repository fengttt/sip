# shortest common super seq

def lkupscs(x, y, m, n, lookup):
    if m == 0:
        return [y[:n]]
    if n == 0:
        return [x[:m]]

    if (m, n) in lookup:
        return lookup[(m, n)]

    if x[m-1] == y[n-1]:
        vs = lkupscs(x, y, m-1, n-1, lookup)
        vss = [s + x[m-1] for s in vs]
        lookup[(m, n)] = vss
        return vss
    else:
        vs1 = lkupscs(x, y, m-1, n, lookup)
        vs2 = lkupscs(x, y, m, n-1, lookup)
        if len(vs1[0]) > len(vs2[0]):
            vss = [s + y[n-1] for s in vs2]
        elif len(vs1[0]) < len(vs2[0]):
            vss = [s + x[m-1] for s in vs1]
        else:
            vss = [s + y[n-1] for s in vs2]
            vss.extend([s + x[m-1] for s in vs1])
        lookup[(m, n)] = vss
        return vss

if __name__ == '__main__':
    X = "ABCBDAB"
    Y = "BDCABA"
    lookup = {}

    print("scs = ", lkupscs(X, Y, len(X), len(Y), lookup))

