def odd(n):
    sum=0
    for i in range(1,n+1):
        if i%2!=0:
            sum=sum+i
    return sum
num=int(input("enter a number"))
result=odd(num)
print(result)