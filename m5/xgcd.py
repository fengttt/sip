def xgcd(a, b):
    olds, oldt, oldr = 1, 0, a
    s, t, r = 0, 1, b
    while r != 0:
        q = oldr // r
        oldr, r = r, oldr - q*r
        olds, s = s, olds - q*s
        oldt, t = t, oldt - q*t

    return oldr, olds, oldt

def mxgcd(a):
    if len(a) == 2:
        r, s, t = xgcd(a[0], a[1])
        return r, [s, t]
    
    r, e = mxgcd(a[1:])
    rr, ss, tt = xgcd(a[0], r)
    ee = [ss]
    for olde in e:
        ee.append(olde * tt)
    return rr, ee 

if __name__ == '__main__':
    a = [4, 8, 12, 34, 28, 16, 18, 20, 24]
    r, e = mxgcd(a)
    print (r, e)
