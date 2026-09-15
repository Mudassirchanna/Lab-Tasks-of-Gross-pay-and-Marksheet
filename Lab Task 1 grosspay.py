"""lab_task
Qno:1 write a python program that ask the user to enter the number of  hours worked and hourly rate.
calculate the total pay to the following rules."""

Hours=float(input("enter the number of hours worked : "))
Rate=float(input("enter the hourly rate : "))

if Hours<=40:
    GrossPay=Hours*Rate 
if Hours>40:
    GrossPay=Hours * (Rate*1.5) 

print(GrossPay) 
