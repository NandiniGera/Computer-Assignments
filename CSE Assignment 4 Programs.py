#Question1
print("Question1")
#defining function for tower of hanoi
def TowerOfHanoi(n, from_rod, to_rod, aux_rod):
    if(n==0):
        return
    TowerOfHanoi(n-1, from_rod, aux_rod, to_rod)
    print("Move disk",n,"from_rod",from_rod,"to_rod",to_rod)
    TowerOfHanoi(n-1, aux_rod, to_rod, from_rod)

#number of discs n:
n=3
TowerOfHanoi(n, 'A', 'C', 'B')

print("--------------------------------------------------------------------------------------")

#Question2
print("Question2")
r = int(input("Enter the number of rows in Pascal's Triangle: "))

#using loops
print("Using loops: ")
for rows in range(1,r+1):
    print('  '*(r - rows),end=' ')#to print space consequently according to the number of rows entered
    count = 1 #Pascal's triangle will start with 1 always
    for i in range(1, rows+1):
        print(count,end='  ') #end with space to give it the shape of triangle

        count = count*(rows - i) // i #// rounds the division into nearest whole number
    print()

#using recursions
print("Using recursions: ")
def PascalTriangle(r,checkr=r):
    if (r==0):
        return
    
    PascalTriangle(r-1,checkr)
    print('  '*(checkr-r),end=' ')#spaces get printed
    count2 = 1 
    for i in range(1, r+1):
        print(count2,end='  ')
        count2 = count2*(r - i) // i
    print()
PascalTriangle(r)

print("--------------------------------------------------------------------------------------")

#Question3
print("Question3")
#taking input from user
a=int(input("Enter a number: "))
b=int(input("Enter another number: "))
#finding quotient and remainder
o=divmod(a,b)
print("(Quotient,Remainder: )",o)
#fulfilling question criterias using built in functions
print("(a)")
print("Is function callable?: ",callable(o))
print("(b)")
print("Are all values non zero?; ",all(v!=0 for v in o))
print("(c)")
t=o+(4,5,6)
t=tuple(filter(lambda x:x<=4,t))
print("Output with filtered values: ",t)
print("(d)")
s=set(t)
print("set: ",s)
print("(e)")
f=frozenset(s)
print("Immutable set: ",f)
print("(f)")
m=max(s)
print("Maximum value in set: ",m)
print("Hash of max value: ",hash(m))

print("--------------------------------------------------------------------------------------")


#Question4
print("Question4")
#creating class
class Student:
    def __init__(self,name,rollno):
        print("Student created!")
        self.name=name
        self.rollno=rollno
    def __del__(self):
        print("Student destroyed!")
#creating objects in class
s1Name=str(input("Enter the name of student 1: "))
s1Rollno=int(input("Enter the roll no of student 1: "))
S1=Student(s1Name,s1Rollno)
s2Name=str(input("Enter the name of student 2: "))
s2Rollno=int(input("Enter the roll no of student 2: "))
S2=Student(s2Name,s2Rollno)
s3Name=str(input("Enter the name of student 3: "))
s3Rollno=int(input("Enter the roll no of student 3: "))
S3=Student(s3Name,s3Rollno)
#calling __del__() function to destroy object
print("Deleting student 3: ")
del S3

print("--------------------------------------------------------------------------------------")

#Question5
print("Question5")
#creating class to store employee's data
class Employees:
    def __init__(self,name,salary):
        print("Employee added")
        self.name=name
        self.salary=salary
    def __del__(self):
        print("Employee destroyed")
    def update(self,salary):
        self.salary=salary
        print("Salary updated")
#adding employees
E1=Employees('Mehak',40000)
E2=Employees('Ashok',50000)
E3=Employees('Viren',60000)
print("(a)")
#updating Mehak's salary
Employees.update(E1,70000)
print("(b)")
#deleting Viren's record
del E3

print("--------------------------------------------------------------------------------------")

#Question6
print("Question6")
#input word by first friend:
word1=str(input('Enter word: '))
word1=word1.lower()     #converts the input string into lower case 
#inputting meaningfull word with same letters by second friend 
word2=str(input('Enter meaningfull word for friendship test!: '))
word2=word2.lower()
#initialising dictionary
def count_dict(word1):
    count = {}
    list1 = list(word1)
    n=len(list1)
    for i in range(n):
        if list1[i] in count:
            count[list1[i]]+=1
        else:
            count[list1[i]]=1
    return count
#performing test
if count_dict(word1)!= count_dict(word2):
    print("Letter not exact, friendship is FAKE!")
else:
    #now check the meaning of input word 
    def userinput():
        ans=str(input("Does the word make sense?(y or n)"))
        if ans=='y':
            print("WOHOO! your friendship is TRUE!")
        elif ans=='n':
            print("OH! the word does not make sense, your friendship is FAKE!")
        else:
            print("ERROR! invalid input. try again ")
    userinput()
    print()
            
    


           
        
        

      
    
