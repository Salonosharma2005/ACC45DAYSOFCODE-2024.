# cook your dish here
for _ in range(int(input())):
    
    h, x, y = map(int, input().split())
    
    remaining_health = h - y
    
    normal_attacks_needed = (remaining_health + x - 1) // x
    
    total_attacks = 1 + normal_attacks_needed
    
    print(total_attacks)