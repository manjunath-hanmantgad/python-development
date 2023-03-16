class Employee:
    # creating init method -- based on A
    def __init__(self,first,last,email,pay):
        '''giving it here so that we dont need define indivudally'''
        self.first=first
        self.last=last
        self.email=first + '.' + last + '@gmail.com'
        # adding pay here
        self.pay=pay
        
    
    def full_name(self):
        return '{} {}'.format(self.first,self.last)
    
    # applying raise for the employee
    
    def raise_income(self):
        self.pay = int(self.pay * 1.10) # increased by 10 %
    

# emp_1 = Employee('M','H',100) # I need to add pay here
# emp_2= Employee('Test','User',200)

emp_1 = Employee('M','H','x',100) # I need to add pay here
emp_2= Employee('Test','User','y',200)


# talks about class variables 

# what kind of data will be shared ?

# hard coding without using class variables

print(emp_1.pay)
print(emp_1.raise_income())
print(emp_1.pay)

# I got the error as :
'''
Traceback (most recent call last):
  File "oops_03.py", line 28, in <module>
    print(emp_1.pay)
AttributeError: 'Employee' object has no attribute 'pay'
'''
# so to fix this I need to add pay in my init class.

# now trying with 

# print(Employee.raise_income(emp_2))
