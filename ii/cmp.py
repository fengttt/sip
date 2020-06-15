from functools import total_ordering
import heapq

@total_ordering
class MyInt(object):
    def __init__(self, n): 
        self.n = n

    def __eq__(self, other): 
        return self.n == other.n

    def __lt__(self, other):
        return self.n > other.n

def CandyCnt(arr, n):
    foo = [MyInt(x) for x in arr]
    heapq.heapify(foo)
    cnt = 0

    for i in range(n):
        top = heapq.heappop(foo)
        cnt += top.n 
        top.n //= 2
        heapq.heappush(foo, top)

    return cnt

if __name__ == '__main__':
    arr = [19, 78, 76, 72, 48, 8, 24, 74, 29]
    print("Cnt = ", CandyCnt(arr, 3))
        


