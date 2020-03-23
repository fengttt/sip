def rotc(n, c):
    cc = ord(c)
    if cc >= ord('a') and cc <= ord('z'):
        return chr((cc - ord('a') + n) % 26 + ord('a'))
    elif cc >= ord('A') and cc <= ord('Z'):
        return chr((cc - ord('A') + n) % 26 + ord('A'))
    else:
        return c

def rot(n, s):
    res = ''
    for c in s:
        res += rotc(n, c)
    return res

def rot13(s):
    return rot(13, s)

if __name__ == '__main__':
    print("abc ->", rot13('abc'))
    print("get it back", rot13(rot13('abc')))
    print("xyz ->", rot13('xyz'))
    print("get it back", rot13(rot13('xyz')))
    print("AbC ->", rot13('AbC'))
    print("get it back", rot13(rot13('AbC')))
    print("xYz ->", rot13('xYz'))
    print("get it back", rot13(rot13('xYz')))






