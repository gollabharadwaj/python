n1=int(input("enter first number"))
n2=int(input("enter last number"))
for i in range(n1,n2+1):
    for j in range(2,i):
        if i%j==0:
            break
    else:
        print(i)    
