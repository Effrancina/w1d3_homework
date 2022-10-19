def greet():
    print("Hi!")
# nothing happens upt till here, cause we haven't called the function
# so now we call it:
greet()
# function is not returning anything up until now, it's just printing

def greet():
    return("Hi!")
# nothing will be printed up until here, so we have to create a variable:
# (so we are calling greet and storing whatever it returns to a variable)
greeting = greet()
print(greeting)


def greet():
    print("Hi!")
greeting = greet()
print(greeting)
# this comes out:
# Hi!
# None
# NB. If your function doesn't have a return statement, it will print "None"


# other example
def greet():
    return("Hi!")

greeting = greet()
print(greeting)
# Now let's add in a name
def greet(name):
    return f"Hi {name}!"
# f is used to format the string instead of using the + "name"

greeting = greet("Mar")
print(greeting)



# to personalise it to suite the time of day:
def greet(name, time_of_day):
    return f"Good {time_of_day} we are having, huh, {name}?"

greeting = greet("Mar", "morning")
print(greeting)


# use a variable and pass that as an argument

def greet(name, time_of_day):
    return f"Good {time_of_day} we are having, huh, {name}?"
# here's our variable:
users_name = input("Please enter your name: ")

greeting = greet(users_name, "morning")
print(greeting)

# scope: what each bit of code can access
def greet(name, time_of_day):
    favourite_number =13
    return f"Good {time_of_day} we are having, huh, {name}?"

users_name = input("Please enter your name: ")
greeting = greet(users_name, "morning")
print(greeting)
print(favourite_number)
# the variable favourite_number is declared in the wrong place, so it doesn't get printed and we get the error NameError: name 'favourite_number' is not defined


# upper puts all letters in name in all caps
def new_greet(name):
    name.upper()