num=int(input("Enter Number : "))

factorial=1
if(num==0):
        print("Factorial = ",1)
elif(num<0):
        print("Factorial  Undefined")
else:
    for i in range(1,num+1):
        factorial=factorial*i
    print("factorial = ",factorial)
