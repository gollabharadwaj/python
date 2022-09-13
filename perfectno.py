
def perfect(n):

    temp=n 
    sum=0
    for i in range(1,n):
       if n%i==0:
         sum=sum+i
    if sum==temp:
        print(sum," is perfect number")
    else:
        print("not a perfect")   

num=int(input("enter a number"))    
result=perfect(num)
print()