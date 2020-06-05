from nltk.corpus import words 

def replace(s, n, z):
    ss = list(s)
    ss[n] = z
    return ''.join(ss)

def buildGraph(n):
    g = {}
    wn = [w for w in words.words() if len(w) == n]
    wn = set(wn)
    for a in wn:
        g[a] = []
    for a in wn:
        for i in range(n):
            for z in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ':
                b = replace(a, i, z)
                if b in wn:
                    g[a].append(b)
    return g

def topath(seen, path):
    if seen[path[-1]] == None:
        return path
    path.append(seen[path[-1]])
    return topath(seen, path)

def bfs(g, s, t):
    ret = [t]
    if s == t:
        return ret
    seen = {s: None}
    prev = [s]
    while len(prev) > 0:
        nlv = []
        for w in prev:
            for nw in g[w]:
                if nw not in seen:
                    nlv.append(nw)
                    seen[nw] = w
                if nw == t:
                    return topath(seen, ret)
        prev = nlv

if __name__ == '__main__':
    g = buildGraph(5)
    print(g['black'])


