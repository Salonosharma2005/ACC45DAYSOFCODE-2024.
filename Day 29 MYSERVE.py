# cook your dish here
T = int(input())

for _ in range(T):
    
    P, Q = map(int, input().split())

    total_serves = P + Q

    if (total_serves // 2) % 2 == 0:
        print("Alice")
    else:
        print("Bob")