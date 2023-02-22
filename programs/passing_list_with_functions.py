'''
Say we have a list of users and want to print a greeting to each. The following example sends a list of names to a function called greet_users(), which greets each person in the list individually:
'''

def greet_users(names):
    """print simple message for users"""
    for name in names:
        msg = f"Hello there {name.title()}"
        print(msg)
        
usernames = ['emiway','bantai']
greet_users(usernames)