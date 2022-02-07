# Membership Operators

# "in" operator 

# list1 = [1,2,3,4,5]
# list2 = [2,10,3,30]

list1 = [1,2,3,4,5]
list2 = [6,10,8,30]

for i in list1:
    if i in list2:
        print("Overlapping")
else:
    print("not overlapping")