"""

#list

#prod_list = ["rava","wheat","rice","Oil","Sugar","rice","Oil"]
#print(prod_list)

#1.append - adding element at the end
#prod_list.append("beans")
#print(prod_list)               #['rava', 'wheat', 'rice', 'Oil', 'Sugar', 'beans']

#2.extend - adding element at the end
#prod_list.extend(["jawari","Moong","soap"])
#print(prod_list)               #['rava', 'wheat', 'rice', 'Oil', 'Sugar', 'beans', 'jawari', 'Moong', 'soap']


#3.insert - adding element at specific location (index)
#prod_list.insert(3,"salt")
#print(prod_list)                #['rava', 'wheat', 'rice', 'salt', 'Oil', 'Sugar', 'beans', 'jawari', 'Moong', 'soap']


#4. delete an element
#prod_list.remove("Moong")  #['rava', 'wheat', 'rice', 'salt', 'Oil', 'Sugar', 'beans', 'jawari', 'Moong', 'soap']
#print(prod_list)           #['rava', 'wheat', 'rice', 'salt', 'Oil', 'Sugar', 'beans', 'jawari', 'soap']

#5 delete first occurence of items in list
#prod_list.remove("rice")    #['rava', 'wheat', 'rice', 'Oil', 'Sugar', 'rice', 'Oil']
#print(prod_list)            #['rava', 'wheat', 'Oil', 'Sugar', 'rice', 'Oil']

#6. pop - delete the  last item from list and give removed item as result
#prod_list.pop()              #['rava', 'wheat', 'rice', 'Oil', 'Sugar', 'rice', 'Oil']
#print(prod_list)             #['rava', 'wheat', 'rice', 'Oil', 'Sugar', 'rice']

#print(prod_list.pop())       #['rava', 'wheat', 'rice', 'Oil', 'Sugar', 'rice', 'Oil']
                              #Oil

#print(prod_list.pop(2))       #rice

#7 clear which delete all from list
#print(prod_list)               #['rava', 'wheat', 'rice', 'Oil', 'Sugar', 'rice', 'Oil']
#prod_list.clear()
#print(prod_list)               #[]


#8. Count - counts the occurence of an elements

#stu_marks = [15,45,15,26,59,36,15,48,1,54,56,89,15,26,35,26,47,75]
#print(stu_marks)                       #(15, 45, 15, 26, 59, 36, 15, 48, 1, 54, 56, 89, 15, 26, 35, 26, 47, 75)
#print(stu_marks.count(15))             #4       - as 15 occur 4 times

#9 sort
#stu_marks.sort()
#print(stu_marks)         #[1, 15, 15, 15, 15, 26, 26, 26, 35, 36, 45, 47, 48, 54, 56, 59, 75, 89]



#tuple  - cannot be change

#emp_id = (101,102,103,104,105,106,107,107,102)
#print(emp_id)

#print(emp_id.count(102))   #2
#print(emp_id.index(107))    #6
#print(emp_id.index(107))



#Set

emp_set = {1,2,3,4,5,6}
#print(emp_set)

#add
emp_set.add(7)
emp_set.add(8)
print(emp_set)

#update
emp_set.update([9,10])
print(emp_set)


===================================

emp_set1 = {1,2,3,4,5,6}
emp_set2 = {1,2,3,6,7,8}

#union
set_Result = emp_set1|emp_set2
print(set_Result)


#intersection
set_Result = emp_set1 & emp_set2
print(set_Result)


#minus
set_Result = emp_set1 - emp_set2
print(set_Result)



#Dictionary

emp = {"A":1,"B":2,"C":3,"D":4,"E":5,"F":6}
#print(type(emp))
#print(emp)

#index
#print(emp["F"])

#keys
#print(emp.keys())

#values
#print(emp.values())

#Modify the Dict
emp ['S']= 10
#print(emp)


#print(emp.pop('D'))
#print(emp)
#print(emp.popitem())
#print(emp)

max = list[0]
for item in list:
    if max < item:
        max = item


marks_List = [20,30,86,29,50]
print(marks_List)

max = marks_List[0]

for marks in marks_List:
    if max < marks:
        max = marks
print(max)

age = [18,34,49,58,26,45]
print(age)

old = age[0]
for older in age:
    if old < older:
        old = older
print(old)

Legnth = [12,13,15,18,12,15]
print(Legnth)

lambu = Legnth[0]

for long in Legnth:
    if lambu < long:
        lambu = long

print(lambu)


numbers = [50, 20, 10, 99, 5]

min_value = numbers[0]

for num in numbers:
    if num < min_value:
        min_value = num

print("Minimum number is:", min_value)

maks_list = [12,45,26,59,14,25]

maxi = maks_list[0]
for ele in maks_list:
    if maxi< ele:
        maxi =ele

print(maxi)



from pandas.io.formats.format import return_docstring

emp_list = [1,2,3,4,5,6,1,2,4,5]

def count_emp_list(list):

    count_dict = {}
    for ele in list:
        if ele in count_dict:
                count_dict[ele] = count_dict[ele]+1
        else:
               count_dict[ele]=1             #1:1,  2:1 , 3:1,
    return count_dict

print(count_emp_list(emp_list))            #{1: 2, 2: 2, 3: 1, 4: 2, 5: 2, 6: 1}



emp_list = {1:100,2:200}

print(emp_list)         #{1: 100, 2: 200}

emp_list[1] = emp_list[1] + 50

print(emp_list)         #{1: 150, 2: 200}





##Strings
#in puthon we dont have special data type for char

name = "Shree Ram Samarth"
print(name)

#way 1
print(name[0])

#way 2 for loop
n = len(name)
for nav in range(0,n):
    #print(name[nav])
    print(name[nav],end=",")

#way3 advanced for loop
name = "Shree Ram Samarth"
for nav in name:
    print(nav)


#Slicing#

#way 1
name = "Om Nmahay Shivay"

#for nami in range(0,9):
    #print(name[nami])

#way2
print(name[0:20:1])    #start:End:step  forword order
print(name[::1])       #start:End:step  forword order
print(name[::-1])      #start:End:step  Reverse order



#split

name = "Shree Ram Samarth"
word = name.split(" ")
print(word)

from pandas.io.formats.format import return_docstring

#day 2 assignment 6
#1.way1
city = "ETLQALabs"
print(city[::-1])

#1.way2
revers_city = ""
for i in city:
    revers_city = i + revers_city
print(revers_city)

#2
city = "ETLQALabs"
print(city[3:8:1])
"""
def has_duplicates(input_list):

    marks =[]
    for i in list:
          if i in marks:
              return "Yes"
          marks.append(i)
          return False

list  = [1,2,3,4,3]
result = has_duplicates(list)
#print("Has Duplicate value : ",result)
"""
def has_duplicates(input_list):
    marks = []
    for i in input_list:
        if i in marks:
            return "Yes"
        marks.append(i)
    return "No"

# Test the function
data_list = [1, 2, 3, 4, 3]
result = has_duplicates(data_list)
print("Has Duplicate value:", result)




list1 = [1, 2, 3, 4, 3,4]

Non_duplicae_List = []
duplicate_list = []

def duplicatcheck():
 for i in list1: #1
        if i in Non_duplicae_List:  #no 1 here, so no duplicate
            duplicate_list.append(i)


        else:
            Non_duplicae_List.append(i)


 if Non_duplicae_List:
     print(duplicate_list)
     return  "Yes"
 else:
     return "No"
print(duplicatcheck())



list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print(list[1:10:2])
print(list[2:10:2])



emp = [1,4,3,19,5]

maxi = emp[0]
for ele in emp:
    if ele > maxi:
        maxi = ele
#print(maxi)



def for_max():
    emp = [1, 4, 3, 19, 5]
    maxi = emp[0]
    for ele in emp:
         if ele > maxi:
             maxi = ele
    print(maxi)
for_max()



for num in range(2, 21):      # outer loop
    is_prime = True
    for i in range(2, int(num**0.5) + 1):   # inner loop
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print(num)



list1 = [ 1,2,3,4,5,1,2,5,5]

def list_ele(list1):
    countlist ={}
    for elem in list1:
        if elem in countlist:
            countlist[elem]+= 1
        else:
            countlist[elem] = 1
    print(countlist)

list_ele(list1)



list1 = [ 1,2,3,4,5,1,2,5,5,2]
list2 = [ 1,5,2,2,1,3,4]
def list_ele(list):
    countlist ={}
    for elem in list:
        if elem in countlist:
            countlist[elem]+= 1
        else:
            countlist[elem] = 1
    return countlist
print(list_ele(list1))
print(list_ele(list2))





s = "Hello, World!"
substring = s[-6:-1]
print(substring)


| W  | o  | r  | l  | d  | !  |
| -- | -- | -- | -- | -- | -- |
| 7  | 8  | 9  | 10 | 11 | 12 |
| -6 | -5 | -4 | -3 | -2 | -1 |


s = "World!"
substring = s[-6:]
print(substring)
# output  World

s1 ="etlqa"
length = len(s1)
print(length)
for idx in range(length):
 print(idx,": ",s1[idx])

i = 0
length = len(s1) # 5
while (i < length):
 print(s1[i])
 i = i + 1



s1 ="etl qa labs"
l = s1.split()
print(l)
['etl', 'qa', 'labs']
revlist = l[::-1]
print(revlist," ")
ans = " ".join(revlist)
print(ans)



s1= "abc" # 65 + 25 = 90
sum = 0
for ch in s1:
    sum = sum +ord(ch)
print(sum)


name = "amit kamaraj"

result = ""
a_count = 0
odd_number = 1
for i in range(len(name)):
   if name[i] == 'a':
      result += str(odd_number)
      odd_number += 2 # Move to the next odd number
   else:
    result += name[i]
print(result)


for i in range(20,50):
 if i % 2 != 0:
     continue
     print(i)

for i in range(20, 50):
   if i % 2 == 0:
       continue
   print(i)  # only odd numbers get printed



for i in range(20,50):
 if i == 40:
       break
 print(i)


for i in range(20, 50):
     if i % 2 != 0 and i != 25:
         print(i)
"""

for i in range(10):
 pass
print(i)
