a=int(input("First angle of triangle"))
b=int(input("Second angle of triangle"))
c=int(input("Third angle of triangle"))
sum = a+b+c
if sum>180 or sum<180:
    print("Triangle not possible")
elif sum==180 and a==b==c:
    print("Equilateral triangle")
elif a or b or c ==90 and sum==180 :
    print("Right angled")
elif a==b or a==c or b==c and sum ==180:
    print("Iscoseles triangle")
else:
    print("Scalene triangle")
