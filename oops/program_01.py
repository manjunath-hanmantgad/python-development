# program to calculate the income tax

'''
Rate	Income for Single Individuals
10%	    Up to $9,875
12%	    $9,876 to $40,125
22%	    $40,126 to $85,525
24%	    $85,526 to $163,300
32%	    $163,301 to $207,350
35%	    $207,351 to $518,400
37%	    $518,401 or more
'''
'''
input:

gross income
number of dependents
'''

# Designing the program using pseudocode

''' 
taxable income = gross income - 12,200 - (2000 * number of dependents
)
tax due = amount calculated from tax table 

print tax due
'''

# creating the inpts

gross_income = input("Enter your gross income in USD : ")
print(gross_income)

# for number of dependents 

number_of_dependents = input("Enter number of dependents : ")
print(number_of_dependents)


# calculate the taxable income 

taxable_icnome = gross_income - 12200 - (2000 * number_of_dependents)
# based on formula 

print(taxable_icnome)
# this gives an error as : ypeError: unsupported operand type(s) for -: 'str' and 'int'

