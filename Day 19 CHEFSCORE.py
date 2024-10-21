# cook your dish here
for _ in range(int(input())):  
    n, x, y = map(int, input().split())  
    if y % x == 0 and y // x <= n:  # Check if Y is divisible by X and quotient is <= N
        print('YES')  
    else:
        print('NO')  