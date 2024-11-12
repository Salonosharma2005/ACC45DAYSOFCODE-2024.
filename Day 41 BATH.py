# cook your dish here
# Number of test cases
T = int(input())

for _ in range(T):
    X, Y = map(int, input().split())
    
    if Y == 0:
        print(0)
    else:
        max_people = X // (2 * Y)
        print(max_people)
