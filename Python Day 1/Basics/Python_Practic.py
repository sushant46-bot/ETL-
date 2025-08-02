

"""
ok = {}
ok [1] = 1
print(ok)

def count_emp_list(input_list):
    count_dict = {}
    for ele in input_list:
        if ele in count_dict:
            count_dict[ele] += 1
        else:
            count_dict[ele] = 1
    return count_dict

emp_list = [1, 2, 3, 4, 5, 1, 3, 4, 3]
ans = count_emp_list(emp_list)
print(ans)

s1 ="etl qa labs"
l = s1.split()
print(l)
['etl', 'qa', 'labs']
revlist = l[::-1]
print(revlist," ",type(revlist))
ans = " ".join(revlist)
print(ans,type(ans))


s1 = "ETLQALABS"
# output => QALAB
startindex = s1.find('Q')
endtindex = s1.find('B')
ans = s1[startindex:endtindex+1:1]
print(ans)


"""


name = "amit kamaraj"

result = ""
a_count = 0
odd_number = 1
for i in range(0,12,2):
 if name[i] == 'a':
     result += str(odd_number)
     #odd_number += 2 # Move to the next odd number
 else:
  result += name[i]
print(result)