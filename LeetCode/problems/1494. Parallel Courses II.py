from heapq import heappush, heappop, heapify
from typing import List
import collections
class Solution:
    def minNumberOfSemesters(self, n: int, relations: List[List[int]], k: int) -> int:
        g = collections.defaultdict(list)
        inds = [0]*(n+1)
        for u, v in relations:
            g[u].append(v)
            inds[v] += 1
        pq = [x for x in range(1, n+1) if inds[x] == 0]
        heapify(pq)
        time = 0
        seen = set()
        while pq:
            time += 1
            count = run = 0
            
            while run < len(pq) and count < k and not inds[pq[run]]: 
                count += 1
                run += 1
                
            while count:
                print('aaa')
                count -= 1
                u = heappop(pq)
                if u in seen: continue
                seen.add(u)
                for v in g[u]:
                    inds[v] -= 1
                    if inds[v] == 0 and v not in seen:
                        heappush(pq, v)
        return time

x = Solution()
x.minNumberOfSemesters(5,[[1,5],[1,3],[1,2],[4,2],[4,5],[2,5],[1,4],[4,3],[3,5],[3,2]],3)
                    
            