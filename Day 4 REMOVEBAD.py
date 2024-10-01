# cook your dish here
from collections import Counter

T = int(input())

for _ in range(T):
    
    N = int(input())  # Size of the array
    
    A = list(map(int, input().split()))  
    
    freq = Counter(A)
    
    max_frequency = max(freq.values())
    
    result = N - max_frequency
    
    print(result)
