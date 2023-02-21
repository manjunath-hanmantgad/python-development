# Looping Through an Entire List

'''
 When you want to do the same action with every item in a list, you can use Python’s for loop.
'''

magicians = ['alice', 'david', 'carolina']
for m in magicians: #“For every magician in the list of magicians, print the magician’s name.”
    print(m)

# printing a message to each magician, telling them that they performed a great trick:

for m in magicians:
    print(f"You did a Great trick {m}")

# Let’s add a second line to our message, telling each magician that we’re looking forward to their next trick:

for m in magicians:
    print(f"You did a Great trick {m}")
    print(f"I cant wait to see your next trick {m}.\n")

# Doing Something After a for Loop

for m in magicians:
    print(f"You did a Great trick {m}")
    print(f"I cant wait to see your next trick {m}.\n")

print(f"Thank you for your tricks {magicians}")

'''
Think of at least three kinds of your favorite pizza. Store these pizza names in a list, and then use a for loop to print the name of each pizza.

Modify your for loop to print a sentence using the name of the pizza, instead of printing just the name of the pizza. For each pizza, you should have one line of output containing a simple statement like I like pepperoni pizza.
Add a line at the end of your program, outside the for loop, that states how much you like pizza. The output should consist of three or more lines about the kinds of pizza you like and then an additional sentence, such as I really love pizza!
'''
pizza = ['pizza-a','pizza-b','pizza-c']
for p in pizza:
    print(p)

for p in pizza:
    print(f"I like {p}")