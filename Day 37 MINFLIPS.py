# cook your dish here
def minimum_flips_to_zero(array):
    n = len(array)
    
    if n % 2 != 0:
        return -1
    
    count_1 = array.count(1)
    count_minus_1 = n - count_1  
    
    current_sum = count_1 - count_minus_1
    
    
    if current_sum == 0:
        return 0
    
    
    flips = abs(current_sum) // 2
    return flips


t = int(input())
for _ in range(t):
    n = int(input())
    array = list(map(int, input().split()))
    result = minimum_flips_to_zero(array)
    print(result)
