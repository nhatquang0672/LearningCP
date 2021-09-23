# https://cses.fi/problemset/task/1072

import math

def two_knights(num):
    a1 = num**2
    a2 = a1*(a1-1)//2
    if num>2:
        a2 -= 4*(num-1)*(num-2)
    return a2
    
    

size = int(input())
for i in range(1, size+1):
    print(two_knights(i))