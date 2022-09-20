def towerofhanoi(n,source,dest,middle):
    if n<1:
        print("please enter a positive integer")
    elif n==1:
        print("Move disk {} from {} to {}".format(n,source,dest))
    else:
        towerofhanoi(n-1,source,middle,dest)
        print("Move disk {} from {} to {}".format(n,dest,middle))  
        towerofhanoi(n-1,middle,dest,source)      
num=int(input("enter he number of disks:"))
towerofhanoi(num,'a','c','b')        