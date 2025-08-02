
#add two numbers
"""
a= 2
b= 5

def addtwonumber(a,b):
    c = a+ b
    print("Sum of Two Numbers is :",c)


addtwonumber(10,20)
addtwonumber(42.6,97.8)


#subtract two numbers

def calculation(a,b,c):
    x= a + b - c
    print("Calculation of this is :",x)

calculation(51,5,6)
calculation(51.5,5.8,6.9)



#datatypes

name = "sainath"

print("type of this is :", type (name))

age = 41

print("type of this is :", type (age))

salary = 420052.56
print("value of this is :", type (salary))



#casting

maths = "45.77"
physics = "95.58"

print("marks in math", type(maths))
print("marks in physics", type(physics))

#totalmarksINT = int(maths) + int (physics)
#print( "total marks is ",totalmarksINT , "type of total marks is :", type(totalmarksINT))

totalmarksfloat = float(maths) + float (physics)
print( "total marks is ",totalmarksfloat,"type of total marks is :", type(totalmarksfloat))


#downcasting   flowt to int  --> need to downcast manually
#upcasting int to float   --> python always in upcasting

a = 50
print (float(a))


a = 50
print (float(a))

b = 54.265
print(b)
print(int(b))

from queue import PriorityQueue

age = 1

if (age >= 18):
    print("you can vote")
print ("out side of IF - can not vote")
print(...)


age = 19

if (age >= 18):
    print("you can vote")

else:

    print("can not vote")
print ("out side of IF-ELSE")



marks = float(input("please input yor marks here ..."))
if (marks >= 85):
    print("first calss")
elif(marks< 85 and marks>= 60):
    print("second class")
elif(marks<60 and marks>35):
    print("third Class")
else:
    print("Failed")


print(range (9))

for y in range(2,10,2):
    print(y)


for x in range(10):
 if x>0:
    print(x)

else:    print("control came out of IF LOOP")
print("control came out of for loop")


num=7
while num <= 10:
    if num >= 5:
           break
    print(num)
    num +=1
print("value came out of loop")

#emp List

empList = ["sushant","Sainath","Smita"]
empList.append("okok")
empList.append("sankettt")
print("type of the empList; " , type(empList))
print("Things in the empList; " , empList)



empset = {"sushant","Sainath","Smita"}

print(empset)


#print list best example
names = []
while True:
    name = input("enter name or enter q to (quit)")

    if name == ("q"):
        break
    names.append(name)
    print(names)


Ranks = []
for i in range(1,10,1):
 Ranks.append(i)

 print(Ranks)


"""