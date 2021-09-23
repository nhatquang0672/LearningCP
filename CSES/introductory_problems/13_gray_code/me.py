# https://cses.fi/problemset/task/2205

def gray_code(n):
    ans = [0]
    for i in range(1, n+1):
        prev = len(ans)
        mask = 1 << (i-1)
        for j in range(prev-1, -1, -1):
            ans.append(mask+ans[j])
    for e in ans:
        print(("{:0%db}"%n).format(e))


num = int(input())
gray_code(num)