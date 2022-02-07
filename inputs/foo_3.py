# taking ultiple inputs using list comprehension 

# 2 inputs at time 

a,b = [int(x) for x in input("Enter 2 values:").split()]
print("first number is :",a)
print("sencond number is:",b)
print()

# taking multiple inputs at time 

z = [int(x) for x in input("Enter multiple values:").split()]
print("Number of list is:",z)