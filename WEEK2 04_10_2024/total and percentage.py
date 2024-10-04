sub1=int(input("enter mark of subject 1 : "))
sub2=int(input("enter mark of subject 2 : "))
sub3=int(input("enter mark of subject 3 : "))
sub4=int(input("enter mark of subject 4 : "))
sub5=int(input("enter mark of subject 5 : "))

max_mark=500
total_mark=(sub1+sub2+sub3+sub4+sub5)
percentage=(total_mark/max_mark)*100

print("totalmark: ",total_mark)
print("percentage :",percentage)
