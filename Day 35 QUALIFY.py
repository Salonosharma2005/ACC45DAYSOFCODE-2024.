# cook your dish here
# Number of test cases
T = int(input().strip())

results = []
for _ in range(T):
    
    X, A, B = map(int, input().strip().split())
    
    total_score = A + 2 * B
    
    if total_score >= X:
        results.append("Qualify")
    else:
        results.append("NotQualify")

for result in results:
    print(result)
