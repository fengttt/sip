def longseq(A, start, flag, lookup):
    if start >= len(A):
        return 0

    if lookup[start][flag] == 0:
        res = 0
        for i in range(start, len(A)): 
            if flag == 1 and A[i-1] < A[i]:
                res = max(res, 1 + longseq(A, i+1, 0, lookup))
            elif flag == 0 and A[i-1] > A[i]:
                res = max(res, 1 + longseq(A, i+1, 1, lookup))
            else:
                res = max(res, longseq(A, i+1, flag, lookup))
        lookup[start][flag] = res
    return lookup[start][flag]

def findlongseq(A, lookup):
    return 1 + max(longseq(A, 1, 1, lookup),
                   longseq(A, 1, 0, lookup))

if __name__ == '__main__':
    A = [8,9,6,4,5,7,3,2,4]
    lookup = [[0, 0] for x in range(len(A))]
    print("LongSeq = ", findlongseq(A, lookup))
