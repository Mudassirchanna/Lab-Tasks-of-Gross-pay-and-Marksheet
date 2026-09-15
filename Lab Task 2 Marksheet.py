""" Lab_task 2
Qno:2:write a python program to create an advanced student marksheet.
the program should:"""

name=input("enter the student name : ")
roll_no=input("enter the student roll no : ")

m1=int(input("enter marks of subject 1 : "))
m2=int(input("enter marks of subject 2 : "))
m3=int(input("enter marks of subject 3 : "))
m4=int(input("enter marks of subject 4 : "))
m5=int(input("enter marks of subject 5 : "))

total_marks=m1+m2+m3+m4+m5
percentage=total_marks/5

if percentage>=80  and percentage<=100:
    grade="A+"
    
elif percentage>=70 and percentage<=79:    
    grade="A"
elif percentage>=60 and percentage<=69:
    grade="B" 
elif percentage>=50 and percentage<=59:
    grade="C"    
elif percentage>=40 and percentage<=49:
    grade="D"
elif percentage<40:
    grade="fail"
if m1 < 40 or m2 < 40 or m3 < 40 or m4 < 40 or m5 < 40 :
    
    result="fail"
else:
    result="pass"    

print(f"Student name : {name}" )
print(f"student roll no : {roll_no}")
print(f"Subject marks individually : {m1} + {m2} + {m3} + {m4} + {m5}")
print(f"Total Marks : {total_marks}")
print(f"Percentage : {percentage}")
print(f"Grade : {grade}")
print(f"result : {result}")


