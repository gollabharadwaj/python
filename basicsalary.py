basicSalary=int(input("Enter the basic salary:"))

if basicSalary<-10000:

     HRA=(10000*20)/100

     DA=(10000*80)/100

elif basicSalary>10000 and basicSalary<=20000:

     HRA=(20000*25)/100

     DA=(20000*90)/100

else:

     HRA=(20000*30)/100

     DA=(20000*95)/100


GrosSalary=basicSalary+HRA+DA

print("GrossSalary:",GrosSalary)
