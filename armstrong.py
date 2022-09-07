n=int(input("Enter a number"))
sum=0
temp=n
while(n!=0):
    i=n%10
    sum=sum+i**3
    n=n//10
if(sum==temp):
    print("it is an armstrong number")
else:
    print("not an armstrong number")    
