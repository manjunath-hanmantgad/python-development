# Given a list of size n, remove all even integers from it.

''' 
using if loop / while loop / list comprehension / flter and lambda functions
'''

list1 = [11,10,21,22,1,2,3]
print(list1)

for i in list1:
    if(i%2 == 0):
        list1.remove(i)

print("new list after removing even numbers is:" , list1)

# using random numbers which are generated automatically 

evenlist = []

numbers = int(input("Enter total numbers:"))
for i in range(1, numbers+1):
    values = int(input("enter %d numbers =" %i))
    evenlist.append(values)

print("numbers are:", evenlist)

evenlist = [j for j in evenlist if j %2 != 0]
print("numbers after removing even numbers are:", evenlist)