# https://cses.fi/problemset/task/1632
# from bisect import bisect_right
import bisect
def movie_festival_II(n, k, times):
    free = [0]*k
    ans = 0
    for s,e in times:
        idx = bisect.bisect_right(free, s)
        if idx == 0:
            continue
        idx -= 1
        del free[idx]
        bisect.insort(free, e)

        ans += 1
    print(ans)

n, k = map(int, input().split())
times = []
for _ in range(n):
    s, e = map(int, input().split())
    times.append((s, e))
times = sorted(times, key = lambda k: k[1])
movie_festival_II(n, k, times)

# 10 5
# 46 95
# 80 90
# 53 78
# 77 79
# 75 94
# 49 87
# 35 72
# 57 69
# 22 99
# 64 95