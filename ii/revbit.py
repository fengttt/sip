def printbits(i):
    print("{0:x}".format(i)) 

def tbl():
    t = []
    for i in range(16):
        bits = [0, 0, 0, 0]
        for j in range(4):
            bits[j] = (i >> j) & 1
        print (i, bits)
        t.append((bits[0] << 3) + (bits[1] << 2) + (bits[2] << 1) + bits[3])
    print (t)
    return t
             
T4 = tbl()

def rev8(i8):
    h1 = i8 & 0xF
    h2 = (i8 >> 4) & 0xF
    return (T4[h1] << 4) + T4[h2]

def revbits(i): 
    b0 = i & 0xFF
    b1 = (i >> 8) & 0xFF
    b2 = (i >> 16) & 0xFF
    b3 = (i >> 24) & 0xFF
    print(b0, b1, b2, b3)
    x0 = rev8(b0)
    x1 = rev8(b1)
    x2 = rev8(b2)
    x3 = rev8(b3)
    print(x0, x1, x2, x3)
    return (rev8(b0) << 24) + (rev8(b1) << 16) + (rev8(b2) << 8) + rev8(b3)

if __name__ == '__main__':
    i = 0x12345678
    printbits(i) 
    printbits(revbits(i)) 

