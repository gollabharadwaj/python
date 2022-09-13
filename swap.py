def swap(n):
    st1=str(n)
    l=[i for i in st1]
    temp=l[0]
    l[0]=l[3]
    l[3]=temp
    st2="".join(l)
    
    return int(st2)
num=int(input("enter a number"))
print("number before swapping is",num)    
result=swap(num)
print("number after swapping is",result)