

# def apple_division(n, arr):
#     total_sum = sum(arr)
#     d = total_sum

#     for i in range(1<<n):
#         tmp_sum = 0
#         for j in range(n, -1, -1):
#             if 1<<j&i != 0:
#                 tmp_sum += arr[j]
#         d = min(d, abs(total_sum - 2*tmp_sum))

#     print(d)
# apple_division(n, arr)

def apple_division_recursion(n, arr):
    ans = float('inf')
    def dfs(a, b):
        nonlocal ans
        if a >= n:
            ans = min(ans, abs(b))
            return
        dfs(a+1, b+arr[a])
        dfs(a+1, b-arr[a])
        
    dfs(0,0)
    print(ans)

n = int(input())
arr = [int(x) for x in input().split(' ')]
apple_division_recursion(n, arr)

