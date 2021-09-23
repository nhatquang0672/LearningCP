# https://cses.fi/problemset/task/1620

def factory_machines_old(n, t, arr):
    max_time = t * arr[0]
    ans = 0
    for time in range(arr[0], max_time+1):
        temp = 0
        for i in range(n):
            temp += time // arr[i]
        if temp >= t:
            ans = time
            break
    print(ans)

def factory_machines(n, t, arr):
    lt, rt = 0, t*arr[0]
    ans = 0
    while lt < rt:
        mt = (lt+rt)//2
        temp = 0
        for i in range(n):
            temp += mt // arr[i]
        if temp < t:
            lt = mt+1
        else:
            rt = mt
    
    print(lt)
        
n, t = map(int, input().split(' '))
arr = [int(x) for x in input().split(' ')]
arr.sort()
factory_machines(n, t, arr)