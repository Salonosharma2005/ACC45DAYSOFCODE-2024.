# cook your dish here
def calculate_catch_time(X, Y):
    return abs(X - Y)  


T = int(input())


for _ in range(T):
    
    X, Y = map(int, input().split())
    
    print(calculate_catch_time(X, Y))