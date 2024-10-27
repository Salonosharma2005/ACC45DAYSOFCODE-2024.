# cook your dish here
def maximise_tastiness(test_cases):
    results = []
    for a, b, c, d in test_cases:
        max_tastiness = max(a, b) + max(c, d)
        results.append(max_tastiness)
    return results

t = int(input())

test_cases = [tuple(map(int, input().split())) for _ in range(t)]

max_tastiness_values = maximise_tastiness(test_cases)
for value in max_tastiness_values:
    print(value)