a, b, c = input(), input(), input()
i = j = k = 0
cur = 'a'
while i<=len(a) and j<=len(b) and k<=len(c):
    if cur == 'a':
        if i == len(a): break
        if a[i] != 'a': cur = a[i]
        i += 1
    elif cur == 'b':
        if j == len(b): break
        if b[j] != 'b': cur = b[j]
        j += 1
    else:
        if k == len(c): break
        if c[k] != 'c': cur = c[k]
        k += 1
print(cur.upper())