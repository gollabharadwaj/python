def fib(n):
    if n==0:
        return 0
    elif n==1 or n==2:
        return 1
    else:
        return fib(n-1)+fib(n-2)        
num=int(input("enter a number"))
print("the fibonacci series from 1 to {}".format(num))
for i in range(num):
    print(fib(i))
