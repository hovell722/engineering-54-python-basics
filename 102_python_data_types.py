# Strings
# Text to characters
# Syntax
# "" and ''


# Define a string

my_string = 'Hey I am a cool String B) '
print(my_string)

# Define its type

print(type(my_string))

# Concatenation
# Adding of 2 strings
joint_string = my_string + 'This is another string'
print(joint_string)

# Eg.2 Concatenation
name = 'James'
welcome_text = 'WELCOME TO SPARRTTTTTAAAAAAA (300)'
print(welcome_text + ' ' + name)
print(welcome_text, name) # overloading the print

# Interpolation
# Inserting a string inside another string
# Or running python inside a string
print(f'WELCOME {name} TO CLASS 54, we are Contested Terrain')

print('WELCOME {} TO CLASS 54, we are Contested Terrain'.format(name))

# Useful Methods
# Are like function but belong to a specific data type
# For example, it would not make sense to try to capitalise integers
example_long_str = '   HELLO, THis is a very BAdly formated text?     '
print(example_long_str)

# Remove trailing white spaces
print(example_long_str.strip())

# Make it lower case
print(example_long_str.lower())

# Make it upper case
print(example_long_str.upper())

# Make only the first character capitalised
print(example_long_str.capitalize())

# Make the first character of each word capitalised
print(example_long_str.title())

# Change the '?' into a '!'
print(example_long_str.replace('?', '!'))

# Chain some methods and:
    # remove trailing white spaces
    # make it nicely formatted with only the first letter capitalised
print(example_long_str.strip().capitalize().replace('?', '!'))

# Create a list with individual words
print(example_long_str.split())

# Casting a string
print(type(str(234)))

