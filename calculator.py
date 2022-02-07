# for simple calculator

# function to add 2 numbers

def add(n1,n2):
    return n1+n2 

# function to subtract 2 numbers

def subtract(n1,n2):
    return n1-n2 

# function to multiply 2 numbers 

def mult(n1,n2):
    return n1*n2 

# function to divide 

def div(n1,n2):
    return n1/n2 

print("Select what operation you need:\n" \
       "1. Add \n" \
       "2. Subtract \n" \
       "3. Multiply \n" \
       "4. Divide\n"   
    )


# take input from user 

select = int(input("Select options from above options:"))

number_1 = int(input("enter 1st number: "))
number_2 = int(input("enter 2nd number: "))

if select ==1:
    print("addition result is:" , add(number_1,number_2))
    
elif select ==2:
    print("subtraction result is:", subtract(number_1,number_2))
    
elif select ==3:
    print("multiplication result is:", mult(number_1,number_2))
    
elif select ==4:
    print("division result is:", div(number_1,number_2))
    
else:
    print("invalid input")