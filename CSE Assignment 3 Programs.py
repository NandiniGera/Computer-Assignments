#Question1 
s=input("Enter a string: ")
d={} #initialising a dictionary
if " " in s:
    words=s.split(" ") #Splits the words in the string entered into a list
    for i in words: 
        if i in d: #Checks if the word is present in the dictionary or not
            d[i]+= 1 
        else:
            d[i]=1 #adds the word to the dictionary
    print("No. of occurences of each word in the string entered is:\n",d)
else:
    characters=list(s) #stores the letters of a word in a list
    for i in characters: 
        if i in d: #checks if the letter is in the dictionary
            d[i] += 1
        else:
            d[i]=1 #adds the letter to the dictionary
    print("No. of occurences of each character in the string entered is:\n",d)



#Question2
while(1):    #condition to enter loop is always true 
    year=int(input("Enter the year"))
    if(1800<=year<=2025): #checks if the year entered lies within the input range as given in question 
        break
    else:
        print("Invalid year entered")
        print("Enter the year again") #input year will be asked again and again until the year within correct range is entered by the user 

while(1):
    month=int(input("Enter the month"))
    if(1<=month<=12):
        break
    else:
        print("Invalid month entered")
        print("Enter the month again")
M1=[1,3,5,7,8,10,12]
M2=[4,6,9,11]
M3=[2]

while(1):
    date=int(input("Enter the date"))
    if(month in M1 and 1<=date<=31):
        break
    elif(month in M2 and 1<=date<=30):#date 31 does not exist in the months having 30 days as list M2 contains
        break
    elif(month in M3 and year%4==0 and 1<=date<=29):#date 29 is also accepted in february if the year entered is a leap year
        break
    elif(month in M3 and year%4!=0 and 1<=date<=28):#date 29 is not accepted in february if the year entered is not a leap year 
        break
    else:
        print("Invalid date entered")
        print("Enter the date again")



if( month in M1):
     if(1<=date<=30):
         nextdate=date+1
         month2=month
         year2=year
     elif(date==31 and month<12):
        nextdate=1
        month2=month+1
        year2=year
     elif(date==31 and month==12):
        nextdate=1
        month2=1
        year2=year+1
     else:
         year2=year
     
    

if( month in M2):
     if(1<=date<=30):
         nextdate=date+1
         month2=month
         year2=year
     else:
        nextdate=1
        month2=month+1
        year2=year
     

if( month in M3):
    if(year%4==0 and 1<=date<=28):
           nextdate=date+1
           month2=month
           year2=year
    if(year%4==0 and date==29):
        nextdate=1
        month2=month+1
        year2=year
    if(year%4!=0 and 1<=date<=27):
        nextdate=date+1
        month2=month
        year2=year
    if(year%4!=0 and date==28):
        nextdate=1
        month2=month+1
        year2=year

        

print("NEXT DATE IS:",nextdate,",",month2,",",year2)


#Question3
#Taking input list
list1=list(map(int,input("Enter the numbers").split()))#input numbers with spaces and they are put into a list
list2=[]
#storing in tuple
for n in list1:
    tuple=(n,n**2)
    list2.append(tuple)
#final result
print("\nList with (n.n^2) is as shown:")
print(list2)



#Question4
while(1): #condition to enter loop is always true
    GradePoints=int(input("Enter the grade point between 4 and 10 including both 4 and 10 as well"))
    if(4<=GradePoints<=10):
        break
    else:
        print("Invalid input")
        print("Enter the grade point again")

if GradePoints==4:
        letterGrade="D"
        performance="Poor"
elif GradePoints==5:
        letterGrade="C"
        performance="Below Average"
elif GradePoints==6:
        letterGrade="C+"
        performance="Average"
elif GradePoints==7:
        letterGrade="B"
        performance="Good"
elif GradePoints==8:
        letterGrade="B+"
        performance="Very Good"
elif GradePoints==9:
        letterGrade="A"
        performance="Excellent"
else:
        letterGrade="A+"
        performance="Outstanding"
print("Your grade is",letterGrade,"and",performance,"performance")
    

#Question5
pattern="ABCDEFGHIJK"
s=" " #defined space
print(pattern)
for a in range(len(pattern)//2+1): 
    pattern=pattern[:len(pattern)-2] #The last 2 letters of the pattern will get removed consequently
    print(" "*a,pattern) #spaces will get increased as the loop runs from both ends 



#Question6
SID=dict() #initialising a dictionary
NAME=dict() #initialising a dictionary

while(1):   #condition to enter loop is always true
    
    sid=int(input("Enter Unique SID: "))#no same sid can be entered 
    name=str(input("Enter the name: "))
    SID[sid]=name 
    NAME[name]=sid 
    CHECK=str(input("Enter 'Y' if you want to input more names and SIDs OR Enter 'N' if you're done with the input"))
              
    CHECK=CHECK.upper() #Converts the string into upper case
    if CHECK=='Y':
        continue #the loop will run again 
    elif CHECK=='N':
        break #exits the loop
    else:
        SID={}
        NAME={}
        print("Invalid input")
        print("Enter Y or N only") 
        

#6(a)
print("6(a)")    
print(SID)

#6(b)
print("6(b)")
for x in sorted(NAME): #Sorts the dictionary in alphabetical order of student names entered by the user
    print(x,NAME[x])

#6(c)
print("6(c)")
for x in sorted(SID): #Sorts the dictionary in the increasing order of SIDs entered by the user
    print(x,SID[x])

#6(d)
print("6(d)")
x=int(input("Enter the SID: "))
if x in SID: 
    print("Name: ",SID[x])
else: 
    print("The SID entered does not exist. ")


#Question7
n=int(input("Enter number of elements N in fibonacci series:\n[N must be positive Integer]: N="))
if n<=0 :
    print("\nError\nNumber of elements in fibonacci series must be an integer and greater than zero.")
else:
    #code for fibonacci series for first 2 elements
    if n == 1:
        print("\nThe fibonacci series with 1 element is shown below\n[1]")
        print("\nAverage of given fibonacci series is", 1)

    elif n == 2:
        print("\nThe fibonacci series with 2 element is shown below\n[1,1]")
        print("\nAverage of given fibonacci series is", 1)
    #General code for fibonacci for next N-2 elements
    else:
        # List of fibonacci elements with 1,1 as initial elements
        list1 = [1, 1]
        a = 1
        b = 1
        # For loop
        for i in range(n - 2):
            s = a + b
            list1.append(s)
            a = b
            b = s
        print(f"\nThe fibonacci series with {n} elements is shown below:")
        print(list1)
        # Finding average of fibonacci series
        sum = 0    #intial sum=0
        # finding sum of all elements in list1
        for num in list1:
            sum = sum + num
        average = (sum / n)
        twodecimal = "{:.2f}".format(average)# Till two decimal place
        print(f"\nAverage of given fibonacci series is {twodecimal}")

#Question8
set1= {1, 2, 3, 4, 5}
set2= {2, 4, 6, 8}
set3= {1, 5, 9, 13, 17}
print(f"Set1= {set1}\nSet2= {set2}\nSet3= {set3}")
#a
print("\nQ.8(a)")
print("\nA new Set of all 'elements that are in Set1 and Set2 but not both' is:",set1^set2)
#b
print("\nQ.8(b)")
print("\nSet of elements that are in only one of the three sets:",set1^set2^set3)
#c
print("\nQ.8(c)")
print("\nA new set of elements that are 'exactly in two of the sets Set1, Set2 and Set3' is:",set1&set2|set2&set3|set1&set3)
#d
print("\nQ.8(d)")
print("\nA new set of all Integers in the 'range 1 to 10' that are 'not in Set1' is:",set(range(1,10))-set1)
#e
print("\nQ.8(e)")
print("\nA new set of all Integers in the range 1 to 10 that are not in Set1,Set2 and Set3.",set(range(1,10))-set1-set2-set3)



    

