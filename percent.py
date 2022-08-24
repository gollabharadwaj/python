a=int(input("Enter the marks scored in maths"))
b=int(input("Enter the marks obtained in physics"))
c=int(input("Enter the marks obtained in chemistry"))
percent=((a+b+c)/300)*100

print("percentage of the student is",percent)
if percent>=90:
  print("Grade A")
elif percent>=80:
  print("Grade B")
elif percent>=70:
  print("Grade C")
elif percent>=60:
  print("Grade D")
elif percent>=40:
  print("Grade E")  
else:
  print("Fail")    
