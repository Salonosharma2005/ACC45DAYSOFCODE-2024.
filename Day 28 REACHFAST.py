# cook your dish here
T = int(input())

for _ in range(T):
    
    A, B, K = map(int, input().split())
    
    distance = abs(B - A)
    
    min_steps = (distance + K - 1) // K

    print(min_steps)
