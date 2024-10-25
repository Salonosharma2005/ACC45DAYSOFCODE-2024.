# cook your dish here
T = int(input())
for _ in range(T):
    N = int(input())
    contest_codes = input().split()
    
    count_start38 = 0
    count_ltime108 = 0
    
    for code in contest_codes:
        if code == "START38":
            count_start38 += 1
        elif code == "LTIME108":
            count_ltime108 += 1
    
    print(count_start38, count_ltime108)