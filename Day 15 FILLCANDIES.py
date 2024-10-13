# cook your dish here
def calculate_bags_needed(N, K, M):
    candies_per_bag = K * M
    if N <= candies_per_bag:
        return 1
    else:
        full_bags = N // candies_per_bag
        if N % candies_per_bag > 0:
            full_bags += 1
        return full_bags

T = int(input())
for _ in range(T):
    N, K, M = map(int, input().split())
    result = calculate_bags_needed(N, K, M)
    print(result)