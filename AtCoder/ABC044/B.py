import collections
def sol(s):
    s = collections.Counter(s)
    for k, v in s.items():
        if k.islower() and v%2 == 1: 
            print('No')
            return
    print('Yes')

s = input()
sol(s)