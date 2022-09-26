arange = range(5)
alist = list(arange) # converting range to list

# to access first element
alist[1]
# to access last element
alist[-1]

# to access using variables
idx = 3
alist[idx] # gets element at 3rd position

alist2 = [4,3,[1,2,3,4],5,[7,8,9]]
alist[2][2] # gets element at 2nd position and then in that list gets 2nd element of that inside list

str1 = 'hello'
str1[1] # gets the character 'e'

list1 = [4,'hi',[1,2],'yo', {'animal':'dog','fish':'flying'}]

# get the flying from list1

list1[4]['fish']
