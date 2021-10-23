def F(b, n):
    r = 0
    while n>0:
        r += n % b
        n = n // b
    return r

def make_divisor(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n%i == 0:
            divisors.append(i)
            if i != n//i: 
                divisors.append(n//i)
    divisors.sort()
    return divisors

def sol(n, s):
    if n-s == 0: return n+1
    elif n < s: return -1
    else:
        A = make_divisor(n-s)
        for i in range(len(A)):
            if F(A[i]+1, n) == s:
                return A[i]+1
        return -1

n, s = int(input()), int(input())
print(sol(n, s))