# sequence control structures = line by line execute karega
# selection control structures = pehle questions puch fir execute kr based on these questions
# iteration control structures = code ko repeatedly execute krega

for iteration in range(5):
    print("Wake up bhai!")
    
# ye tha definite iteration jaha malum hai kabhi khatam hoga 
# loop ka

# random program 

# names = []
# tucontinue = ""

# while tucontinue != "N":
#     name = input("Enter your name")
#     print(name)
#     names.append(name) # new name ko append kro name variable mai
#     tucontinue = input("continue (Y or N)")

# print(names)    

# suppose I want this to run only twice even if it says 'Y'

names = []
tucontinue = ""
count = 0

while count < 2 and  tucontinue != "N":
    name = input("Enter your name")
    print(name)
    # name ko count mai append kro
    count += 1
    names.append(name) # new name ko append kro name variable mai
    tucontinue = input("continue (Y or N)")
print(names)  