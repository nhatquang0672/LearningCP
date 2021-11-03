N, K = map(int, input().split())
if N == 1: print(K)
else: print(K*(K-1)**(N-1))