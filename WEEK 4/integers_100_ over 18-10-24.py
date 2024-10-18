list=[]
size=int(input("Enter The number of integers to be added "))

for i in range (size):
    integers=int(input(f"enter integer {i+1}:"))
    list.append(integers)
for i in range(len(list)):
                 if list[i]>100:
                     list[i]='over'
                  
print("list =",list)
