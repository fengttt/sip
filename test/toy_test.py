import siplib.toy as toy

def test_sum():
    for i in range(1, 100):
        assert toy.sumint(i) == i*(i+1)/2 
        assert toy.sumodd(i) == i*i
        
def test_even():
    for i in range(1, 100):
        assert toy.sumint(i) * 2 == toy.sumeven(i)
        
