 #Question1
inpstr="Python is a case sensitive language" #inpstr=input string as given in question
#a
print("The length of string is", len(inpstr)) #function to find the length of the string
#b
print("The reverse string is",inpstr[::-1])
#c
inpstr2=inpstr[10:26]#stored "a case sensitive" in another string
print(inpstr2)
#d
inpstr2.replace("a case sensitive","object oriented") #replaced "a case sensitive" with "object oriented"
#e
print("The index of substring a is ", inpstr.find('a'))
#f
print("The original string without spaces is",inpstr.replace(" ",""))



#Question2
Name="Nandini"
SID="21103035"
Department="ComputerScience"
CGPA="9.9"
print("Hey,", Name, "Here!","\n","My SID is", SID,"\n","I'm from", Department,"Department and my CGPA is", CGPA)#as directed in question



#Question3
a=56
b=10 #given in question
print("Given a=",a,"\n","b=",b)
#a
print("The value of a&b is ",a&b)
#b
print("The value of a|b is ",a|b)
#c
print("The value of a^b is ",a^b)
#d
print("Left side both a and b with 2 bits respectively are:",a<<2,b<<2)
#e
print("Right shift a with 2 bits and b with 4 bits respectively are:",a>>2,b>>4)



#Question4
n1=float(input("Enter the first number:" ))
n2=float(input("Enter the second number:" ))
n3=float(input("Enter the third number:" ))
if(n1>=n2 and n1>=n3):
       print("The largest number among these three is",n1)
elif(n2>=n1 and n2>=n3):
       print("The largest number among these three is",n2)
else:
       print("The largest number among these three is",n3)




#Question5
s=input("Enter a string")#s stores the string entered by the user
if 'name' in s:#checkes whether "name" is part of string entered by user
    print("Yes")
else:
    print("No")



#Question6
a=int(input("Enter the first side of triangle" ))
b=int(input("Enter the second side of triangle" ))
c=int(input("Enter the third side of triangle" ))
if(a>(b+c)):
    print("No,triangle cannot be formed")
elif(b>(a+c)):
    print("No,triangle cannot be formed")
elif(c>(a+b)):
    print("No,triangle cannot be formed")
else:
    print("Yes,triangle can be formed")
    


       

