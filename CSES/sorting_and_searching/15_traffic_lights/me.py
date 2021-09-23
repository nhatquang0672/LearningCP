# https://cses.fi/problemset/task/1163

from bisect import bisect_left

def traffic_lights(x, n, pp):
    tt = [0, x]
    ll = [x]
    for e in pp:
        pos = bisect_left(tt, e)
        tt.insert(pos, e)
        left, right = tt[pos-1], tt[pos+1]
        ll.insert(bisect_left(ll, e-left), e-left)
        ll.insert(bisect_left(ll, right-e), right-e)
        del ll[bisect_left(ll, right-left)]
        print(ll[-1])

x, n = map(int, input().split(' '))
pp = [int(x) for x in input().split(' ')]
traffic_lights(x, n, pp)