from nltk.corpus import words 

def replace(s, n, z):
    ''' replace replaces the n-th letter in string s with letter z '''
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
    ''' bfs is breadth-first-search on graph g, starting with s, trying to reach target t '''
    ret = [t]
    if s == t:
        return ret
    # seen is a map records that if we have already visited it before.   
    # seen[a] == b means, we will visit a, from b.
    # seen[s] == None, means, s is the starting point
    seen = {s: None}
    # Prev, are the nodes that I visisted, but their neighbour I have not explored yet.
    prev = [s]
    # len(prev) > 0 means, search is not finished yet (because I still have nodes in prev to examine).
    while len(prev) > 0:
        # nlv, the next level.
        nlv = []
        # for each word in prev, which is the previous level.   Prev level, means we visited prev loop,
        # but have not explored their neighbours.
        for w in prev:
            # nw in , g[w] which is, a list of nodes that is neighbor of w 
            for nw in g[w]:
                # if nw has not been seen before,
                if nw not in seen:
                    # we put nw in next level.
                    nlv.append(nw)
                    # Now we mark nw as seen, from w.
                    seen[nw] = w
                # if nw == t, means we found the target.
                if nw == t:
                    return topath(seen, ret)
        # Note here we are still in the while loop.   
        prev = nlv
    # we examined everything, out of the while loop, not found yet,
    return None

def dfs(g, s, t): 
    ''' dfs is the depth-first-search on graph g, start from s, trying to reach t. '''
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
    g = buildGraph(6)
    print(g['autumn'])

    print("BFS: ", bfs(g, 'autumn', 'winter'))
    # print("DFS: ", dfs(g, 'spring', 'winter')) 
