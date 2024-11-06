dict1={'Name':'abdul janeeb k','Roll No':5, 'registration Number':'676307','Department':'MCa','Sem':1}
print("Dictionary :",dict1)
print()

dict1['Total Mark']=int (input("Enter Mark Out Of 100 :"))
print("Dictionary After Adding Total Mark :",dict1)
print()

if dict1['Total Mark']>=90:
    dict1['Grade']='A'
elif dict1['Total Mark']>=82:
    dict1['Grade']='B'
elif dict1['Total Mark']>=60:
    dict1['Grade']='C'
elif dict1['Total Mark']>=50:
    dict1['Grade']='D'
else:
    dict1['Grade']='F'

print("Dictionary After Adding grade : ",dict1)
print()

dict1.pop('Roll No')
print("Dictionary after deleting roll number : ",dict1)
    
    
