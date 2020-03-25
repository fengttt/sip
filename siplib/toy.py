def gcd(a, b):
    '''Return greatest common divisor of a and b'''
    if a == 0:
        return b
    elif b == 0:
        return a
    return gcd(b, a%b)


def diskArea(r):
    return 3.1416 * r * r

def squareArea(s):
    return s*s

def triangleArea(s):
    return 1.732 / 4 * s * s

def sumint(n):
    '''Return sum of the first n natural numbers.'''
    s = 0
    for i in range(n):
        s += i+1
    return s

def sumodd(n):
    '''Return sum of the first n odd natural numbers.'''
    s = 0
    for i in range(n):
        s += i*2 + 1
    return s

def fib(n):
    '''Return n-th fib number.'''
    a, b = 1, 1
    while n > 1:
        a, b = b, a+b
        n -= 1
    return b

def writeCharAt(s, idx, c):
    '''Return s with idx-th char replaced with c'''
    l = list(s)
    l[idx] = c
    return ''.join(l)
