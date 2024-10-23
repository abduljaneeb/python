string=input("Enter A String :")
first=string[0]

result=first+string[1: ].replace(first,"&")
print("result string :",result)
