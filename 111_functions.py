# Functions

# A function is like a machine
# It can take in inputs
# And do some work (block of code)
# And it can output something different
# They need to be called to work

#Calling a function is just writing the name and passing

# Functions - Good Practices
# They do ONE job
# They should be testable and maintainable
# Good naming conventions
# Generally NEVER print inside a function
# ### The above avoid STRING code - Spaghetti code
# Reduce technical debt

# Concept of DRY
# Don't
# Repeat
# Yourself

# Syntax

# def name_of_function(arg1, arg2):
    # block of code
    #
    # return 'doing some work'

# defining a simple function
def  say_hello_zeus():
    return 'hello zeus'

# calling AND printing a function
print(say_hello_zeus())

# Defining a function with arguments
## Arguments are variables that exist in the scope of a function

def full_name_formatter(f_name, l_name):
    formatted_f_name = f_name.strip().capitalize()
    formatted_l_name = l_name.strip().capitalize()
    # Format each name nicely
    # I can use .strip and .capitalize
    # I have access to the name via the arguments f_name and l_name
    # Save these into variables
    # Return a joined full name that is correctly formatted
    # Join the two variables into one string
    full_name = formatted_f_name + ' ' + formatted_l_name
    # Return said string
    return full_name

# Call function with names
print(full_name_formatter('    JamES','   hOVELL'))

def add_function(num1, num2):
    # I want to return the addition of two numbers
    # I have access to num1 and num2
    # I can save result in a variable
    return num1 + num2

print(add_function(4, 3))