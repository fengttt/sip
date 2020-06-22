import matplotlib.pyplot as plt
import numpy as np

def factor2(n):
    if n == 1:
        return [(1, 1)]
    ret = []
    for i in range(1, n+1):
        if n % i == 0:
            ret.append((i, n//i))
    return ret
        
class Poly(object):
    def __init__(self, a):
        if a == None or len(a) == 0:
            self.a = [0]
        else:
            self.a = a.copy()
        self.normalize()

    def normalize(self):
        while self.a[-1] == 0 and len(self.a) > 1:
            self.a.pop()

    def termstr(self, ai, i):
        if i == 0:
            return str(ai)

        if ai == 0:
            return ""

        sign = "+"
        if ai < 0:
            sign = "-"
            ai = -ai

        if i == 1:
            return f" {sign}{ai}x"
        else:
            return f" {sign}{ai}x^{i}"

    def __str__(self):
        return "".join([self.termstr(self.a[i], i) for i in range(len(self.a))])

    def __call__(self, x):
        ret = 0
        xnth = 1
        for i in range(len(self.a)):
            ret += self.a[i] * xnth
            xnth *= x
        return ret
    
    def __add__(self, other):
        ''' self + other '''
        
    def __sub__(self, other):
        ''' self - other '''

    def __mul__(self, other):
        ''' self * other '''

    def factor(self):
        ''' for poly of order 2 or 3, return factors '''
        
    def order(self):
        ''' a0 + a1 x + a2 x^2 ... an x^n return return n'''
        return len(self.a)
    
    def plot(self, lo, hi):
        ''' plot the curv, with x range from lo to hi'''
        xs = np.linspace(lo, hi, 200)
        ys = [self.__call__(x) for x in xs]
        plt.plot(xs, ys)
        plt.show()

if __name__ == '__main__':

    p1 = Poly([1, 2, 3])
    p2 = Poly([-1, 6, -7, 0, -8, 9, -2])
    p3 = Poly([0, -1, 6, -7, 0, -8, 9, -2])
    p4 = Poly([])
    p5 = Poly([5])
    p6 = Poly([1, 3, 5, 0, 0])

    print("p1 =", p1, "p1(2) = ", p1(2))
    print("p2 =", p2)
    print("p3 =", p3)
    print("p4 =", p4)
    print("p5 =", p5)
    print("p6 =", p6)

    p1.plot(-10, 10)
    p2.plot(-1, 1)
