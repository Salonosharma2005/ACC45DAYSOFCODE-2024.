# cook your dish here
def pass_or_fail(T, test_cases):
    results = []
    for i in range(T):
        N, X, P = test_cases[i]
        total_score = 4 * X - N
        if total_score >= P:
            results.append("PASS")
        else:
            results.append("FAIL")
    return results

# Example usage
T = int(input())
test_cases = [tuple(map(int, input().split())) for _ in range(T)]
results = pass_or_fail(T, test_cases)

# Output results
for result in results:
    print(result)
