from collections import Counter

def palindrome_reorder(counter):
    first_part = ""
    last_part = ""
    center = ""
    for e in counter:
        first_part += e*(counter[e]//2)
        last_part = e*(counter[e]//2) + last_part
        if counter[e] % 2 == 1:
            if len(center):
                print('NO SOLUTION')
                return
            else:
                center += e
    print(first_part+center+last_part)

counter = Counter(input())
palindrome_reorder(counter)
