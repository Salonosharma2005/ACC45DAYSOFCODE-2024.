# cook your dish here
def chef_tv_subscription_cost(test_cases):
    results = []
    for case in test_cases:
        N, X = case
        
        subscriptions_needed = (N + 5) // 6
        
        total_cost = subscriptions_needed * X
        results.append(total_cost)
    return results

T = int(input())

test_cases = []
for _ in range(T):
    N, X = map(int, input().split())
    test_cases.append((N, X))

results = chef_tv_subscription_cost(test_cases)

for result in results:
    print(result)
