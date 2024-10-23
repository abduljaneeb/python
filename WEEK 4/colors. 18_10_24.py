list1=[]
size=int(input("Enter number of colors to be added :"))
for i in range(size):
         colors=input(f"enter colours {i+1}:")
         list1.append(colors)
new_list=[list1[0],list1[-1]]
print("list of colours :",list1)
print("New list :",new_list)
