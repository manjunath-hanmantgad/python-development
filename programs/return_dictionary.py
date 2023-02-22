"""
A function can return any kind of value you need it to, including more complicated data structures like lists and dictionaries. For example, the following function takes in parts of a name and returns a dictionary representing a person:
"""

def make_person(first_name,last_name):
    """return dictionary of person"""
    person = {'first':first_name , 'last':last_name}
    return person 

rapper = make_person('emiway','bantai')
print(f"My fav rapper is {rapper}")