# cook your dish here
T = int(input())

for _ in range(T):
    
    N = int(input())
    
    coefficients = list(map(int, input().split()))

    degree = -1
    for i in range(N):
        if coefficients[i] != 0:
            degree = i  

    print(degree)
  