# cook your dish here
T = int(input())

for _ in range(T):
    
    A, B, C = map(int, input().split())
    
    total_price = A + B + C - min(A, B, C)
    
    print(total_price)
