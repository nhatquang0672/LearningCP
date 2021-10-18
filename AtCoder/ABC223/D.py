from collections import defaultdict, deque
from heapq import heapify, heappush, heappop

v, n = map(int, input().split())
es = [[int(x) for x in input().split()] for _ in range(n)]
ins = defaultdict(int)
adjs = defaultdict(list)
ans = []
visited = set()

for e1, e2 in es:
    adjs[e1].append(e2)
    ins[e2] += 1

dq = [v1 for v1 in range(1, v+1) if ins[v1] == 0]
heapify(dq)

while dq:
    target = heappop(dq)
    if target in visited: continue
    ans.append(target)
    visited.add(target)
    for v2 in adjs[target]:
        ins[v2] -= 1
        if ins[v2] == 0 and v2 not in visited:
            heappush(dq, v2)

if len(ans) == v:
    print(*ans)
else:
    print('-1')

