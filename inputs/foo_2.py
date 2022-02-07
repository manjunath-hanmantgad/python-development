# Taking multiple inputs from user in Python

""" 
2 options are available to take multiple inputs

-> using split()
-> using list comprehension
 
"""

# using split function 

# taking 2 inputs at time 

a, b = input("Enter 2 values: ").split()

print("Number of apples :", a)
print("Number of balls:", b)
print()

# taking 3 inputs 

a,b,c = input("enter 3 values:").split()
print("Number of apples:",a)
print("Number of balls:",b)
print("Number of cats:",c)
print()

# taking multiple inputs at single time 

a, b = input("enter 2 values:").split()

print("number of apples is {} and number of balls is {}".format(a,b))
print()

# also can use map function 

d = list(map(int,input("enter values:").split()))
print("list of numbers :", d)