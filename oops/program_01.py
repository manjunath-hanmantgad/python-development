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

# modifying the input to look better


gross_income = input("Enter your gross income in USD : ")
#print(gross_income)
print("Your gross income is :" + gross_income + ".")
# assigning as int and str 

gross_income_float = float(gross_income)

# for number of dependents 

number_of_dependents = input("Enter number of dependents : ")
#print(number_of_dependents)
print("You have " + number_of_dependents + " dependents." )
number_of_dependents_float = float(number_of_dependents)

# calculate the taxable income 

# taxable_icnome = gross_income - 12200 - (2000 * number_of_dependents)
# based on formula 

#print(taxable_icnome)
# this gives an error as : ypeError: unsupported operand type(s) for -: 'str' and 'int'

taxable_icnome = gross_income_float - 12200 - (2000 * number_of_dependents_float)
#print(taxable_icnome)
#print("Your taable income is " + taxable_icnome + ".")
# getting the error as :
# TypeError: can only concatenate str (not "float") to str

# to fix this:
print("Your taxable income is " + str(taxable_icnome) + ".")

tax_due = taxable_icnome * 0.1 
#print(tax_due)
#print("Your tax due is :" + str(int(tax_due)) + ".")

# but taxing is done from a formula
# so using conditional statements

# pseudo code 

'''
1. calculate 10% of income
2. calculate 12% of remaining income 
3. calculate 22% of remaining amount
4. add these 3 values
5. there are other brackets as well
like 24%,32%,35%
'''

# decalaring the variables 

max10 = 9875
max12 = 40125
max22 = 85525
max24 = 163300
max32 = 207350
max35 = 518400
 
tier10_tax = max10 * .1 
tier12_tax = tier10_tax + ((max12 - max10) * .12)
tier22_tax = tier12_tax + ((max22 - max12) * .22)
tier24_tax = tier22_tax + ((max24 - max22) * .24)
tier32_tax = tier24_tax + ((max32 - max24) * .32)
tier35_tax = tier32_tax + ((max35 - max32) * .35)


# calculating tax due 

if taxable_icnome <=max10:
    tax_due = taxable_icnome * 0.1
elif taxable_icnome <=max12:
    tax_due = tier10_tax + ((taxable_icnome - max10) * .12)
elif taxable_icnome <=max22:
    tax_due = tier12_tax + ((taxable_icnome - max12) * .22)
elif taxable_icnome <=max24:
    tax_due = tier24_tax + ((taxable_icnome - max24) * .24)
elif taxable_icnome <=max32:
    tax_due = tier32_tax + ((taxable_icnome - max32) * .32)
elif taxable_icnome <=max35:
    tax_due = tier35_tax + ((taxable_icnome - max35) * .35)
elif taxable_icnome > max35:
    tax_due = tier35_tax + ((taxable_icnome - max35) * .37)
    
#print(int(tax_due))
print("Your tax due is :" + str(int(tax_due)) + ".")