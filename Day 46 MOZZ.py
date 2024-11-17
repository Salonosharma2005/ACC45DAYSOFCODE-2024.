# cook your dish here
import math
T = int(input())

for _ in range(T):
    
    X, Y, R = map(int, input().split())
    
    total_sticks_eaten = X + (R // 30)
    
    max_plates = math.ceil(total_sticks_eaten / Y)
    print(max_plates)