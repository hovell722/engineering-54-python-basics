# # Create a little program that ask the user for the following details:
#  - Name
#  - height
#  - favourite color
#  - a secrete number

user_name = input("What is your name? ")
user_height = int(input("What is your height in cm? "))
user_colour = input("what is your favourite colour? ")
user_animal = input("What is your favourite animal? ")
user_secret = int(input("Now give me a secret number. "))

# Capture these inputs
# Print a tailored welcome message to the user
# print other details gathered, except the secret of course

print(f"Hello {user_name}, you are a {user_height}cm tall, {user_colour} {user_animal}.")

# hint, think about casting your data type.