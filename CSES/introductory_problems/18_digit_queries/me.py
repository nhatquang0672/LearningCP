import math

def digit_queries(num):
    i = 1
    size_char = 1

    if num < 10:
        print(num)
        return

    while (10**i-10**(i-1))*size_char < num :
        num -= size_char*((10**i-1) - 10**(i-1) + 1)
        size_char += 1
        i += 1
    
    quotient = num // size_char if num % size_char == 0 else num // size_char+1

    final_num = 10**(i-1)+quotient-1

    fIndex = num - (quotient-1)*size_char

    # print(quotient, final_num, num, fIndex, size_char)

    print(str(final_num)[fIndex-1])

n = int(input())
for i in range(n):
    num = int(input())
    digit_queries(num)