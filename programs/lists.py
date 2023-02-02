# Accessing Elements in a List

bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)
print(bicycles[1:-2])
print(bicycles[2])
print(bicycles[1:])

# Using Individual Values from a List

message = f"My first bicycle was {bicycles[1]}."
print(message)

# Modifying Elements in a List

'''
 To change an element, use the name of the list followed by the index of the element you want to change,
and then provide the new value you want that item to have.
'''
bicycles_modified = ['trek', 'rockrider', 'redline', 'specialized']
print(bicycles_modified)
bicycles_modified[1] = 'rocky2'
print(bicycles_modified)

# Appending Elements to the End of a List
'''
When you append an item to a list, the new element is added to the end of the list.
'''

bicycles_modified.append('rocky3')
print(bicycles_modified)

# Inserting Elements into a List
'''
You do this by specifying the index of the new element and the value of the new item:
'''

bicycles_modified.insert(4, 'rocky4')
print(bicycles_modified)

bicycles_modified.insert(3, 'rocky4')
print(bicycles_modified)

# using appned , insert and delete methods

print(f"I like the {bicycles_modified[0]} , "
      f"but I love to ride the newly added {bicycles_modified.insert(0, 'rocky10')} , "
      f"so I will remove the {bicycles_modified.remove('redline')} from my collection.")

# Sorting a List Permanently with the sort() Method

cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)
#print(cars.sorted()) #AttributeError: 'list' object has no attribute 'sorted'. Did you mean: 'sort'?

''' .sort() modifies the original list and returns None'''


# sort this list in reverse-alphabetical order by passing the argument reverse=True

cars.sort(reverse=True)
print(cars)

# using sorted

print(sorted(cars))

print('**************')
#print(f"Here is original list: {cars.sort(reverse=False)}") # this gives None
cars_2 = cars.sort(reverse=True) # this also returns None
# read : https://stackoverflow.com/questions/61174535/simple-python-question-why-cant-i-assign-a-variable-to-a-sorted-list-in-place
print(cars_2)
print(f"Here is original list: {cars_2}")
print(f"Here is sorted list:{sorted(cars)}")