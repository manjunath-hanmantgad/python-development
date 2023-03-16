# sequence control structures = line by line execute karega
# selection control structures = pehle questions puch fir execute kr based on these questions
# iteration control structures = code ko repeatedly execute krega

# for iteration in range(5):
#     print("Wake up bhai!")
    
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

# names = []
# tucontinue = ""
# count = 0

# while count < 2 and  tucontinue != "N":
#     name = input("Enter your name")
#     print(name)
#     # name ko count mai append kro
#     count += 1
#     names.append(name) # new name ko append kro name variable mai
#     tucontinue = input("continue (Y or N)")
# print(names)


###################

# string operations 

# message = "Hello bhai kaisa hai ?"
# print(message.split()) # bracket nhi dala to sirf address dega

# print(message[:3]) # matlab ye pehle se start krega and word ka indes se
# # matlab iska start hoga 0 - H , 1 - e , 2 - l , 3 - l , 4 - o
# # and aage se.

# # string searching 
# # using 'in' keyword 
# # string matching is done # matlab case sensitive hai

# for i in message:
#     print(i)


# loop ke andar loop 

# employees = ['E1', 'E2', 'E3']
# for i in employees:
#     print(i)
#     for k in i:
#         print(k.upper())
#     print("-----------")

fruit_list = ["apple", "banana", "cherry", "gooseberry", "kumquat", "orange", "pineapple"]
for fruit in fruit_list:
    print(fruit)