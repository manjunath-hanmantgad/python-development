def greeter():
    """a function which greets people"""
    print("Hello")

greeter()

# Passing Information to a Function

def greeter(username):
    """provide username """
    print(f"Hello, {username.title()} ")

greeter('andy')


# Arguments and Parameters

# username is called as parameter [info needed by function to do its job]
# andy is called as argument [which is passed to function]

def favorite_book(title):
    print(f"One of my favorite books is: {title.title()}")
favorite_book('Alice in Wonderland')