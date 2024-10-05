# cook your dish here
def check_monopoly(T, test_cases):
    results = []
    
    for profits in test_cases:
        P, Q, R, S = profits
        total_profit = P + Q + R + S
        
        if (P > total_profit - P or 
            Q > total_profit - Q or 
            R > total_profit - R or 
            S > total_profit - S):
            results.append("YES")
        else:
            results.append("NO")
    
    return results
    
def main():
    T = int(input())
    test_cases = []
    
    for _ in range(T):
        profits = list(map(int, input().split()))
        test_cases.append(profits)
        
    results = check_monopoly(T, test_cases)
    
    print("\n".join(results))

if __name__ == "__main__":
    main()