import math
n = int(input())
curT, curA = map(int, input().split())
for i in range(n-1):
    rT, rA = map(int, input().split())
    factor = max((curT-1)//rT+1, (curA-1)//rA+1)
    curT, curA = rT*factor, rA*factor
print(curT+curA)