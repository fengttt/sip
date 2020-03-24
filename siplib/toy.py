def gcd(a, b):
    if a == 0:
        return b
    elif b == 0:
        return a
    return gcd(b, a%b)


def diskArea(r):
    return 3.1416 * r * r

def squareArea(s):
    return r*r

def triangleArea(s):
    return 1.732 / 4 * s * s

def sum(n):
    s = 0
    for i in range(n):
        s += i+1
    return s

def sumodd(n):
    s = 0
    for i in range(n):
        s += i*2 + 1
    return s

def fib(n):
    a, b = 1, 1
    while n > 1:
        a, b = b, a+b
        n -= 1
    return b

def writeCharAt(s, idx, c):
    l = list(s)
    l[idx] = c
    return ''.join(l)
