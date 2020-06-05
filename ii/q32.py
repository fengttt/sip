def opt(freq, i, j, lv, mem):
    if j < i:
        return 0

    key = (i, j, lv)
    if key not in mem:
        cost = float('inf') 
        for k in range(i, j+1):
            lcost = opt(freq, i, k-1, lv+1, mem)
            rcost = opt(freq, k+1, j, lv+1, mem)
            cost = min(cost, freq[k] * lv + lcost + rcost)
        mem[key] = cost
    return mem[key]


if __name__ == '__main__':
    freq = [25, 10, 20]
    print("Opt cost = ", opt(freq, 0, 2, 1, {}))
