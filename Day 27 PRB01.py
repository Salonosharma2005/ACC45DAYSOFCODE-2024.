# cook your dish here
t1 = int(input())
for i in range(t1):
    n = int(input())
    k1=0
    for i in range(1,(n+1)) :
        if n%i==0:
            k1+=1
   
    if k1==2:
        print ("yes")
    else:
        print("no")