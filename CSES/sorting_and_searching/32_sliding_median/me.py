# https://cses.fi/problemset/task/1076

from heapq import heappop, heappush
import math

def sliding_median(n, x, arr):
    maxl = []
    minr = []
    ans = []
    med = (x+1)//2
    m = 0

    for idx, val in enumerate(arr):
        
        if m < med:
            heappush(minr, (val, idx))
            nv, ni = heappop(minr)
            heappush(maxl, (-nv, -ni))
            m += 1
        else:
            heappush(maxl, (-val, -idx))
            nv, ni = heappop(maxl)
            heappush(minr, (-nv, -ni))

        while minr and minr[0][1] <= idx-x: heappop(minr)        
        while maxl and -maxl[0][1] <= idx-x: heappop(maxl)
        
        if idx < x-1:
            continue

        ans.append(-maxl[0][0])        
        if arr[idx-x+1] <= -maxl[0][0]:
            m -= 1

    print(' '.join(str(x) for x in ans))

n, x = map(int, input().split())
xx = [int(x) for x in input().split()]
sliding_median(n, x, xx)