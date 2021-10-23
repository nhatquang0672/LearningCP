def sol(s):
    for i in range(len(s)-1):
        if s[i] == s[i+1]:
            print(i+1, i+2)
            return
        if i+2<len(s) and s[i] == s[i+2]:
            print(i+1, i+3)
            return
    print(-1, -1)

s = input()
sol(s)