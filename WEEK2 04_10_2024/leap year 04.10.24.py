current_year=int(input("enter current year : "))
final_year=int(input("Enter Final Year : "))
print("leap years : ")
for i in range(current_year,final_year):
    if((i%4==0) and (i%100!=0) or (i%400==0)):
        print(i)
