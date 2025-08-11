from operator import truediv

import pandas as pd
from decorator import append
from sqlalchemy import false
from sqlalchemy.util.typing import is_origin_of
from win32con import DISPLAY_DEVICE_PRIMARY_DEVICE

'''

#print(pd.read_csv("employees.csv"))


set1 = {1,2,3,4,5,6}
set2 = {1,2,4,5,6,7}

output = set1.intersection(set2)
print(output)


emp = "rakesh"
series = list(emp)
print(series)
'''
"""
Write a function to check if list contains any duplicate element and return True or False as
applicable
def has_duplicates(lst):  # Define the function
    seen = []             # An empty list to keep track of seen items
    for item in lst:      # Loop through each item in the input list
        if item in seen:  # If the item is already seen
            return True   # Found a duplicate, so return True
        seen.append(item) # Otherwise, remember this item
    return False          # If no duplicates found, return False





def method1(emp):
    s1 = []
    for i in emp:
        if i in s1:
         return True
        print (i)
        s1.append(i)
        print(i)
    return False

emp = [1, 2, 3, 4, 5, 1, 3]
print(method1(emp))


# same with better aoproch
def find_duplicates():
    seen = set()
    duplicates = set()

    for i in emp:
        if i in seen:
            duplicates.add(i)   # collect duplicate
        else:
            seen.add(i)

    if duplicates:
        print("Duplicates found:", duplicates)
        return True
    else:
        print("No duplicates found")
        return False

emp = [1, 2, 3, 4, 5,1,3]
print(find_duplicates())


List = [1,2,3,4,5,1,3]

rows = {}

for i in List:
    if i in rows:
        rows[i] += 1
    else:
        rows[i]=1

print(rows)









N = int(input("Enter the Number"))
list1 =[]
for j in range(2,N): #(N**0.05)
 is_prime = True
 for k in range(2, int(j**0.5) + 1):  #
     if j % k ==0:
        is_prime = False
        break
 if is_prime:
     list1.append(j)
print(list1)



actuallist = [1,2,3,3,4,4,5]
duplist = []
uniqlist = []
def duplicatelist(actuallist):

 for  i in actuallist():
    if i in uniqlist:
        duplist.append(i)
    else:
        uniqlist.append(i)




actual = [1,2,3,4,5]
add = 0
for i in actual:
     add += i
print(add)






n = int(input("input the number: "))
list1=[]

for i in range(2,n):
    is_prime = True

    for j in range(2, int(i**0.5)+1):
        if i % j == 0:
            is_prime = False
            break

    if is_prime:
        list1.append(i)

print(list1)

n = int(input("Enter Number Here:"))
prime_list = []

for i in range(2,n):
    is_prime = True
    for j in range(2,int(i**0.5)+1):
        if   i % j ==0:
            is_prime = False
            break

    if is_prime:
        prime_list.append(i)

print(prime_list)



n= int(input("input Number Here:"))
Prime_number = []


for i in range(2,n):
    is_prime = True
    for j in range(2,int(i**0.5)+1):
        if i % j ==0:
            is_prime = False
            break
    if is_prime:
        Prime_number.append(i)
print(Prime_number)



x=int(input("Enter the number here:"))
prime_num = []

for i in range(2,x):
       is_prime = True
       for j in range  (2,int(i**0.5)+1):
           if i % j ==0:
               is_prime = False
               break
       if is_prime:
        prime_num.append(i)
print(prime_num)




x= int(input("Enter Number here: "))
prime_num = []
is_prime = True

if x<=1:
    is_prime = false
else:
      for j in range  (2,int(x**0.5)+1):
           if x % j ==0:
               is_prime = False
               break
print(is_prime)



"""
