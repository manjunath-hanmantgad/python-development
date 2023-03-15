
# we have a company
# represent the employyes via this class
# each employee wll have different attributes 

class Employee:
    # creating init method -- based on A
    def __init__(self,first,last,email):
        '''giving it here so that we dont need define indivudally'''
        self.first=first
        self.last=last
        self.email=first + '.' + last + '@gmail.com'
    
    def full_name(self):
        return '{} {}'.format(self.first,self.last)
        
        

# each employee will be attibute of this class employee

''' 
emp_1 = Employee()
emp_2 = Employee()
'''

# now creating based on class

emp_1 = Employee('M','H',1)
emp_2= Employee('Test','User',1)

# there was error that I need to give 3 arguments or inputs
# when calling the emp_1.email
# but when I gave something else in 3rd position then 
# it did not throw the error.





# print(emp_1) # different addresses
# print(emp_2)

# # employees have fist and last names

# emp_1.first = "M"
# emp_1.last = "H"
# emp_1.email = "MH@gmail.com"
# emp_1.pay = 100


# emp_2.first = "Test"
# emp_2.last = "User"
# emp_2.email = "TestUser@gmail.com"
# emp_2.pay = 200

print(emp_1.email)
print(emp_2.email)

# so rather than manually doing this 
# need to set it up in the initail stage itself.

# using __init__ method -- A

# now to get full name
# but without class

#print('{} {}'.format(emp_1.first,emp_1.last))

# so creating a method for full name in the class 

# now getting full name using above function 

print(emp_1.full_name)
print(emp_2.full_name)

# if I do this I get method but not the method

# so to get the data
print(emp_1.full_name())
print(emp_2.full_name())

# running the methods using the class names itself.

print(Employee.full_name()) # this complains of missing self.
#print(Employee.full_name(self)) # self is not defined
print(Employee.full_name(emp_1))

emp_1.full_name() # no need to pass self as emp_1 will be picked up
Employee.full_name(emp_1) # need to pass , as self will not pick up by itself.
