n,k=[int(i) for i in input().split()]
a=[int(i) for i in input().split()]
b=[0]*1000007
b[0]=1
for i in range(k):
    b[i]%=1000000007
    if b[i]>0:
        for j in a:
            if i+j<=k : b[i+j]+=b[i]
print(b[k]%1000000007)