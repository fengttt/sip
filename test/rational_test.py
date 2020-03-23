from siplib.rational import Rational

def test_ctr():
    assert Rational(1) == Rational(2, 2)
    assert Rational(0) == Rational(0, 2)
    assert Rational(0).isZero()
    assert Rational(-1, -3).isPositive()
    assert Rational(2, 4) == Rational(3, 6)
    
def test_xxx():
    x = Rational(1, 6)
    y = Rational(8, 24)
    z = Rational(-5, -10)

    assert x+y+z == Rational(1)

