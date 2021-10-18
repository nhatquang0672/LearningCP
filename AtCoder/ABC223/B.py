def sol(s):
    ans = [s]
    for i in range(1, len(s)):
        ans.append(s[i:]+s[:i])
    ans = sorted(ans)
    print(ans[0])
    print(ans[-1])
s = input()
sol(s)