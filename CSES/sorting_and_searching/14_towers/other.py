import bisect
 
 
import bisect
n = int(input())
l = list(map(int,input().split()))
d = []
for i in l:
    y = bisect.bisect_right(d,i)
    if y==len(d):
        d.append(i)
    else:
        d[y] = i
 
print(len(d))