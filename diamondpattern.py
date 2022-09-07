n=6
for i in range(1,n):
    for j in range(1,i+1):
            print("*",end=" ")
    print(end="\n")
for i in range(1,n): 
    for j in range(1,n):
        if j<n-i:
           print("*",end=" ")   
    print(end="\n")
