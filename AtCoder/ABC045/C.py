a = input()
def cal(s, prev):
    tmp = 0
    if not s: return prev
    for i in range(1,len(s)+1):
        tmp += cal(s[i:], prev+int(s[:i]))
    return tmp
print(cal(a, 0))