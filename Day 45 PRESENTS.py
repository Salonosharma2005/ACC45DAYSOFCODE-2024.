# cook your dish here
def minimum_coins(T, test_cases):
    results = []
    for N in test_cases:
        coins = 4 * (N // 5) + (N % 5)
        results.append(coins)
    return results

T = int(input())
test_cases = [int(input()) for _ in range(T)]

results = minimum_coins(T, test_cases)
for res in results:
    print(res)
