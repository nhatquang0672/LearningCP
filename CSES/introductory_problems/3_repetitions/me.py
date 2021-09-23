# https://cses.fi/problemset/task/1069

def repititions(s): 
    ans, cur = 0, 1
    for i in range(1,len(s)):
        cur = cur+1 if s[i] == s[i-1] else 1
        ans = max(ans, cur)

    print(max(ans, cur))

if __name__ == '__main__':
    s = input()
    repititions(s)