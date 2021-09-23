# https://cses.fi/problemset/task/1635

C = 1000007

def coin_combinations_I(n, x, coins):
    mem = [0]*C
    mem[0] = 1
    for i in range(x):
        if mem[i] > 0:
            for c in coins:
                if i+c <= x:
                    mem[i+c] += mem[i]
                    mem[i+c] = mem[i+c] % 1000000007

    print(mem[x])
n, x = map(int, input().split())
arr = [int(x) for x in input().split()]
coin_combinations_I(n, x, arr)

# 100 1000
# 389 101 552 795 876 269 887 103 154 689 542 920 128 541 44 657 310 531 656 567 386 536 900 374 929 505 255 376 384 709 311 404 699 86 512 518 321 916 408 935 568 662 731 933 238 331 833 235 423 352 205 669 413 152 695 713 878 614 109 164 387 3 287 823 485 716 556 323 924 57 35 705 643 77 200 944 768 490 589 339 701 190 714 349 252 303 74 526 186 644 453 251 429 170 777 216 22 825 514 379