# cook your dish here
T = int(input())  # Read the number of test cases
for _ in range(T):
    N, K = map(int, input().split())
    characteristics = list(map(int, input().split()))
    wolverine_count = 0
    for value in characteristics:
        if (value + K) % 7 == 0:
            wolverine_count += 1
    print(wolverine_count)