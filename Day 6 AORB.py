# cook your dish here
def max_points(T, test_cases):
    results = []
    
    for X, Y in test_cases:
        
        points_a_first = (500 - 2 * X) + (1000 - 4 * (X + Y))
        
        
        points_b_first = (1000 - 4 * Y) + (500 - 2 * (X + Y))
        
        
        results.append(max(points_a_first, points_b_first))
    
    return results

T = int(input())  
test_cases = [tuple(map(int, input().split())) for _ in range(T)]

results = max_points(T, test_cases)

for result in results:
    print(result)
