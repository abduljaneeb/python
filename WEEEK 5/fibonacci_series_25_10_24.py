list1=[]
a=0
b=1
size=int(input("Enter length of fibonacci series : "))
for i in range(size):
    list1.append(a)
    a,b=b,a+b
print("Fibonacci series : ",list1)    
