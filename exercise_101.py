# Practice String
# Welcome to Sparta - exercise

# Version 1 specs - with concatenationj
# Define a variable name, and assign a string with a name

welcome_message = 'Welcome to my code!'


# Prompt the user to input and ask the user for his/her name

user_name = input("What is your name? ")

# Use concatenation to print a welcome message and use method to form the name/input

print(welcome_message, user_name)

# Version 2

# Ask the user for a first name, save it in a variable

first_name = input("What is your first name? ")

# Ask the user for a last name, save it in a variable

last_name = input("What is your last name? ")

# Do the same but use a different message and
# Use interpolation to print the message

print(f"WE ARE CONTESTED TERRAIN AND YOU ARE {first_name} {last_name}! However, in SQL you would be {last_name} {first_name}.")