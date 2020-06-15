from nltk.corpus import words 

def replace(s, n, z):
    ss = list(s)
    ss[n] = z
    return ''.join(ss)

def buildGraph(n):
    g = {}
    wn = [w for w in words.words() if len(w) == n and w.lower() == w]
    wn = set(wn)
    for a in wn:
        g[a] = []
    for a in wn:
        for i in range(n):
            for z in 'abcdefghijklmnopqrstuvwxyz':
                b = replace(a, i, z)
                if b != a and b in wn:
                    g[a].append(b)
    return g

def topath(seen, path):
    while True:
        if seen[path[-1]] == None:
            return path
        path.append(seen[path[-1]])
    return path

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


def dfs(g, s, t): 
    seen = {s: None}
    stack = [s] 
    while len(stack) > 0:
        n = stack.pop()
        for nn in g[n]:
            if nn not in seen:
                seen[nn] = n
                if nn == t:
                    return topath(seen, [t])
                stack.append(nn)
    return None

if __name__ == '__main__':
    g = buildGraph(5)
    print(g['black'])

    print("BFS: ", bfs(g, 'black', 'white'))
    print("DFS: ", dfs(g, 'black', 'white')) 
