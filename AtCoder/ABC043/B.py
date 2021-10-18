arr = list(input())
ans = []
for c in arr:
    if c == '0' or c == '1':
        ans.append(c)
    else:
        if ans: ans.pop()
print(''.join(ans))