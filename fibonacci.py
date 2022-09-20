def fib(n):
    first,second=0,1
    for i in range(n):
        if i<=1:
            result=i
        else:
            result=first+second
            first=second
            second=result    
    print(result)
num=int(input("enter a number:"))    
print("The fibonacci series fro 1 to {}".format(num))
fib(num)          