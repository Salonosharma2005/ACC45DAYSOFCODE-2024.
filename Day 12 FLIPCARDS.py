# cook your dish here
T = int(input())

for _ in range(T):
    
    N, X = map(int, input().split())
    
    min_flips = min(X, N - X)
    
    print(min_flips)