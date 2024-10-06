# cook your dish here
T = int(input())  

for _ in range(T):
    X, Y = map(int, input().split())  
    
    K = (Y - 1) // X  
    print(K) 