a=input("enter first number")
b=input("enter second number")
c=input("enter third number")
d=(int(a)+int(b)+int(c))/3
print("the average of three numbers is :")
print(float(d))


Standard_deduction=10000
dependent_deductions=3000
gross=input("Enter your gross income")
No_of_dependents=input("Enter your number of dependents")
taxable_income =int(gross)-int(Standard_deduction)-(int(dependent_deductions)*int(No_of_dependents))
tax=(float(taxable_income)*0.2)
print("Your income tax is :")
print(float(tax))


SID=input("Enter your SID")
Name=input("Enter your name")
Gender=input("Enter your gender")
Course_name=input("Enter your course name")
CGPA=float(input("Enter your CGPA"))
STUDENT=[SID,Name,Gender,Course_name,CGPA]
print(STUDENT)


marks1ststudent = int(input("Marks of 1st student : "))

marks2ndstudent = int(input("Marks of 2nd student : "))

marks3rdstudent = int(input("Marks of 3rd student : "))

marks4thstudent = int(input("Marks of 4th student : "))

marks5thstudent = int(input("Marks of 5th student : "))

SortedMarks = [marks1ststudent, marks2ndstudent, marks3rdstudent, marks4thstudent, marks5thstudent]

SortedMarks.sort()# to sort the lsit in a order.

print(SortedMarks)





color=['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
print(color)
# (a) Python program to print a specified list after removing 4th element.
del color[3]  # 3 is index to 4th element of color list
print("output of part a is:")
print(color)
# (b) Remove ‘Black’ and ‘Pink’ from the list and replace them with ‘Purple’.
# Do that in one line code.
# index of black is 3 and index of pink is 4
print("output of part b is:") 
color=['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
color[3:5]=["Purple"]   #replace 3 to 4 items to "Purple"
print(color)
