def sol(n, arr):
    total_t = 0
    for l, v in arr:
        total_t += l/v
    meet_t = total_t / 2
    ans = 0
    for l, v in arr:
        if meet_t < l/v:
            ans += meet_t*v
            print(ans)
            return
        ans += l
        meet_t -= l/v
    

n = int(input())
arr = []
for i in range(n):
    arr.append([int(x) for x in input().split()])
sol(n, arr)