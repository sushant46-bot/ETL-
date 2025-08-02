

'''
name = "Sushant"
print("Type of name is ", type (name))
age  = "30"
print("Type of age is ", type (age))
workinginIt = True

print("Type of workinginit is ", type (workinginIt))


salaryPerMonth = 10000.40
print("Type of salaryPerMonth is ", type (salaryPerMonth))

print(name,age,workinginIt,salaryPerMonth)
'''

'''
#casting (converting data from one data type to other)

markinMaths = "70"
markinPyscis = "95"

print("Type of marks in Maths", type(markinMaths))
print("Type of marks in Physcis", type(markinPyscis))


#conver to int
totalmarksINT = int (markinMaths) + int(markinPyscis)
print("type of marks",type(totalmarksINT)," and the total marks is", totalmarksINT)

totalmarksINT = float (markinMaths) + float(markinPyscis)
print("type of marks",type(totalmarksINT)," and the total marks is", totalmarksINT)
---------------------------------------------------------------------------------
#downcasting and upcasting

num1 = 50
num2 = 20
print ("additon is", num1 + num2 )


num3 = 50.50
num4 = 20.30
print ("additon with downcasting  is", num1 + num2 )
'''



'''
#control statment
#if , else  if ,

age = 58

if (age >= 18):
    print("printing inside ....")
    print("person is eligible to vote")
print("printing outside...")

-------------------------------------------------------------------------------------
#else:

age = 8

if (age >= 18):
    print("printing inside ....")
    print("person is eligible to vote")

else:
    print("Not eligible")
'''
'''
#if....elif.esle

marks = int(input("Enter Your Marks Here : "))

if (marks >= 65):
    print("first grade")
elif (marks >= 35 and marks <65):
    print("second grade")
elif (marks >= 35 and marks <65):
    print("third grade")
else:
    print("Fail")
print("Result is Decleared")

'''

#Range Function
#print(range (9))
'''
#looping contruct
# for loop while loop
print(1)
print(2)
print(3)
print(4)
print(5)
print(6)
'''

'''
#print  from 0 to n-1
for x in range(5):
    print(x)
'''

'''   
# to ignore the starting from 0 then use if function
#range(start index, End index,step)
#here by default start index 0 and step is 1
for x in range(5):
 if x>0:
    print(x)
print(...)

for x in range(1,5,1):
     print(x)
print(...)

#for odd numbers
for x in range(1, 10, 2):
    print(x)
print(...)

#for even numbers
for x in range(2, 10, 2):
    print(x)
print(...)


for x in range(2, 11, 2):
    print(x)
print(...)


#while loop for odd numbers

num=1
while num <= 10:
    print(num)
    num = num + 2

#collections : group of things / items

#List  [] -- store group of items (emmid), can store duplicates values and can add , remove item from list (mutable)
#Tuple () -- store group of items (emmid), can store duplicates values but can not add or remove items from tuple (imutable)
#set   {} -- store group of items (emmid), will never accept Duplicate values (mutable) but order of data keeps changing
#Disctionary  -- store group of items with key and value paire.,g (empid : empname)


empList = ["sushant","Sainath","Smita"]

print("type of the empList; " , type(empList))
print("Things in the empList; " , empList)

#add one more name
empList.append("Shankar")

print("Things in the empList; " , empList)

#Remove one more name
empList.remove("sushant")

print("Things in the empList; " , empList)



# to specificaly fine person from list let say last guy from list

empList = ["sushant","Sainath","Smita"]
l = len(empList)
print(l)
print(empList[l-1])

#using for loop, we can print the list ------ need to check this again
#for x in range (0,l,1)
 #   print(empList[x])

 #tuple#
empTuple = ("sushant", "sainath", "Smita")
print(type(empTuple))
print(empTuple)
print(...)



#SET no duplicate values here (in this if Smita and smita name is here it will take both as Capital letter S)
empSET = {"sushant", "sainath", "Smita","smita"}
print(type(empSET))
print(empSET)


#methods of list

empList = [1,2,3,4,5]
print(empList)

print(empList.pop(0))
print(empList)
print(empList.pop(3))
print(empList)


empList = [1,2,3,4,5,6,7,8,9,10,2,5,6,7,1,3,2]

print(empList)
print(empList.count(2))

empList = [1,6,7,8,9,10,2,3,4,5]
print(empList)
empList.sort()
print(empList)
empList.reverse()
print(empList)

#tuple methods

emp_tuple = (1,2,3,4,5,6,7,8,9,4,2,6,7)
print(emp_tuple)

print(emp_tuple.count(4)) # 4 comes with 2 times , is hows occures of items

print(emp_tuple.index(5)) #shows index of valus 5 as 4




emp_set = {1,2,3,4,5,6,7,8,9,4,2,6,7}   # out put is - {1, 2, 3, 4, 5, 6, 7, 8, 9} without duplicates
print(emp_set)

#add elements
emp_set.add(55)
print(emp_set)   #op - {1, 2, 3, 4, 5, 6, 7, 8, 9, 55}

emp_set.update([57,78,45,12])
print(emp_set)     #op - {1, 2, 3, 4, 5, 6, 7, 8, 9, 12, 45, 78, 55, 57}




#set therory

set1 ={1,2,3,4,5}
set2 ={3,4,5,6,7}

#union
set_result = set1| set2
print(set_result)    # op - {1, 2, 3, 4, 5, 6, 7}

#intersection
set_result = set1 & set2
print(set_result)    #op - {3, 4, 5}

#Minus
set_result = set1 - set2
print(set_result)    #op - {1, 2}



#Dictnory

emp_dict = {1:"A",2:"B",3:"C"}
print(type(emp_dict))
print(emp_dict)


#get emp name of emp 3
print(emp_dict[2])

#key lie 1 , 2

keys = emp_dict.keys()
print(keys)    #dict_keys([1, 2, 3])

#values
values = emp_dict.values()
print(values)   #dict_values(['A', 'B', 'C'])

#add mofify the dict

emp_dict[5] = "S"
print(emp_dict)    #{1: 'A', 2: 'B', 3: 'C', 5: 'S'}

emp_dict[1] = "S"
print(emp_dict)    #{1: 'S', 2: 'B', 3: 'C', 5: 'S'}

#delete from dict POP
emp_dict.pop(2)
print(emp_dict)   #{1: 'S', 3: 'C', 5: 'S'}

emp_dict.popitem()
print(emp_dict)   #{1: 'S', 3: 'C'}




emp_dict = {1:"A",2:"B",3:"C"}
print(type(emp_dict))
print(emp_dict)

for key, values in emp_dict.items():
    print(key,"----->>>>", values)


marks_list = [55,89,45,36,21,59]
marks_list.sort()
print(marks_list)  #[21, 36, 45, 55, 59, 89]

#way 1
no_of_emenents= len(marks_list)
print(no_of_emenents)   #6


#way 2 without function 

marks_list = [55,89,45,36,21,59]
max= marks_list[0]  #20
for ele in marks_list:
    if max < ele: #89< 50
        max = ele  #89

print(max)
'''
'''
#way 3 with function

#def getmax(marks_list):
    marks_list = [55, 89, 45, 36, 21, 59]
   max= marks_list[0]  #20
   for ele in marks_list:
    if max < ele: #89< 50
        max = ele  #89

print(max)    need to check and correct
'''

#String set of charecters we dont have data type for characters in Python, so we hav singl element string as char
name = "ETL QA Labs"
first_char = "E"
print(type(name))
print(name)
print(first_char)
print(type(first_char))


#how to print each cahr from string

#way 1 indexing
print(name[0])   #E

#way2  for loop

for char in range(0,n):
    print(name[char])









