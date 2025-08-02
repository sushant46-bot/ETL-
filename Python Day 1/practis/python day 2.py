"""

assigmnet
Q1
#with for loop
num = 1

for i in range (1,5):
         num = num*i

print("Result of Multiplication is :", num)

# with while loop
num = 1
i = 1
while i in range(5):
    num = num * i
    i = i + 1

print("Out put with while :" , num)


#Q2

for i in range (1,9,2):
     if (i==1):
        i=i+1
        print(i)  # this logic to print for 2 value
     else:
        print(i)  # this logic to print for rest 3,5,7 value




N = int(input("Enter N: "))

print("Prime numbers using for loop:")
for num in range(2, N + 1):  # Start from 2 because 1 is not prime
    is_prime = True
    for i in range(2, int(num ** 0.5) + 1):  # Check divisibility
        if num % i == 0:
            print("control inside if loop")
            is_prime = False
            print("no is NOT  Prime",num)
        #print("inner loop is break")
            break
    if is_prime:
        print("number is Prime : ",num)
    #print("still into outer LOOP")

from adodbapi.apibase import pythonTimeConverter

vegitables = ("apple","banana","kiwi","pomegrand","Grapes")
for veggis in vegitables:
    print(veggis)


marks = (49,65,89,12,45,68,97,84,52)
for top in marks:
    print(top)

num = 0
for total in range(1,16):
    num +=  total
    print(num)



marks = 0

for i in range(1,10):
    marks += i
    print(marks)


num = (1,2,3,4,5)

for i in num:
 print(i ** 2)



n= 12345
s = str(n)
print (s)
#print(len(s))

for i in s:

    print(len(s))



n = str(12345)

c= 0

for i in n:
    c += 1
print(c)

text = "12345"
i = 0

while i < len(text):
    i += 1

print("Length of string:", i)


n = str(12345)
count = 0

for digit in n:
    count += 1

print("Number of digits using for loop:", count)



n = 12345
i = 0
temp = n

while temp > 0:
    i += 1
    temp //= 10   # Remove last digit

print("Number of digits using while loop:", i)





count = 0
s = int(input("Input INT here :"))
for i in range(1,s+1):
   count += i
print(count)



count = 0
i = 0
s = int(input("Input INT here :"))
while i <= s:
   count += i
   i = i + 1
print(count)

"""



