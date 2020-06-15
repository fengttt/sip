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
        print("A = ", self.a)
        while self.a[-1] == 0 and len(self.a) > 1:
            self.a.pop()
            print("Pop : ", self.a)

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


if __name__ == '__main__':
    p1 = Poly([1, 2, 3])
    p2 = Poly([-1, 6, -7, 0, -8, 9, -2])
    p3 = Poly([0, -1, 6, -7, 0, -8, 9, -2])
    p4 = Poly([])
    p5 = Poly([5])
    p6 = Poly([1, 3, 5, 0, 0])

    print("p1 =", p1)
    print("p2 =", p2)
    print("p3 =", p3)
    print("p4 =", p4)
    print("p5 =", p5)
    print("p6 =", p6)

    for i in range(1, 20):
        print("f2", i, "=", factor2(i)) 
