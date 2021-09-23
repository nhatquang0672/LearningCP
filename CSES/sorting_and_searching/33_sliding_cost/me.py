# https://cses.fi/problemset/task/1077

from heapq import heappush, heappop

def sliding_cost(n, k, arr):
    maxl = []
    minr = []
    ans = []
    med = (k+1)//2
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
        
        while maxl and -maxl[0][1] <= idx-k: heappop(maxl)
        while minr and minr[0][1] <= idx-k: heappop(minr)

        # print(maxl, minr, idx, med)

        if idx < k-1:
            continue
        
        # get median, calculate cost
        cur_med = -maxl[0][0] if k%2 == 1 else (-maxl[0][0]+minr[0][0])/2
        cur_cost = 0
        for e in arr[idx-k+1:idx+1]:
            cur_cost += abs(cur_med-e)
        ans.append(cur_cost)

        if arr[idx-k+1] <= -maxl[0][0]: m -= 1

    print(' '.join(str(int(x)) for x in ans))


n, k = map(int, input().split())
xx = [int(x) for x in input().split()]
sliding_cost(n, k, xx)