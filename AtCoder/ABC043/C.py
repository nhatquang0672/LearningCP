n = int(input())
arr = [int(x) for x in input().split()]
s = sum(arr)
target = s//n
ans0 = ans1 = 0
for num in arr:
    ans0 += (num-target)**2
    ans1 += (num-target-1)**2
print(min(ans0, ans1))