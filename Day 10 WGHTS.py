# cook your dish here
T = int(input())

for _ in range(T):
    
    W, X, Y, Z = map(int, input().split())
    
    possible_weights = {X, Y, Z, X + Y, X + Z, Y + Z, X + Y + Z}
    
    if W in possible_weights:
        print("YES")
    else:
        print("NO")