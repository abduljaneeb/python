list=[]
dict={}
size=int(input("enter number firstname: "))

for i in range(size):
         fname=input(f"enter first name {i+1} :")
         list.append(fname)
for i in list:
         count=i.lower().count("a")
         dict[i]=count

print("first name : ",list)
print('number of occurance of "a" : ',dict)
                               

                        

