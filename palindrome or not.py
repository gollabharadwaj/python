def pal(n):
    
    temp=n
    rev=0
    while n!=0:
        d=n%10
        rev=rev*10+d
        n=n//10
    if rev==temp:
        print(rev," is palindrome")
    else:
        print("not a palindrome")
    return rev
num=int(input("enter a number"))
result=pal(num)
print()                