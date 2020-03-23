def gcd(a, b):
    if a == 0:
        return b
    elif b == 0:
        return a
    return gcd(b, a%b)


class Rational:
    def __init__(self, a, b = 1):
        if b == 0:
            raise "Inavlid rational: div by zero"
        self.num = a
        self.denom = b
        self.simplify()


    def simplify(self):
        if self.num == 0:
            self.denom = 1
            return

        if self.denom < 0:
            self.denom = -self.denom
            self.num = -self.num

        if self.num > 0:
            g = gcd(self.num, self.denom)
        else:
            g = gcd(-self.num, self.denom)
        self.num //= g
        self.denom //= g 

    def isZero(self):
        return self.num == 0

    def isPositive(self):
        return (self.num > 0 and self.denom > 0) or (self.num < 0 and self.denom < 0)

    def isNegative(self):
        return (self.num > 0 and self.denom < 0) or (self.num < 0 and self.denom > 0)


    def negate(self):
        return Rational(-self.num, self.denom)
    
    def __add__(self, other):
        return Rational(self.num * other.denom + self.denom * other.num, self.denom * other.denom)

    def __sub__(self, other):
        return self.__add__(other.negate())

    def __mul__(self, other):
        return Rational(self.num * other.num, self.denom * other.denom)

    def __div__(self, other):
        return Rational(self.num * other.denom, self.denom * other.num)

    def __str__(self):
        return "{0}/{1}".format(self.num, self.denom)

    def __eq__(self, other):
        r = self.__sub__(other)
        return r.isZero()

    def __lt__(self, other):
        r = self.__sub__(other)
        return r.isNegative()

    def __gt__(self, other):
        r = self.__sub__(other)
        return r.isPositive() 

