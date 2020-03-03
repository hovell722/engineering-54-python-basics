# Define the following variables
# name, last_name, species, eye_color, hair_color
# name = 'Lana'

name = 'James'
last_name = 'Hovell'
species = 'Human'
eye_colour = 'Hazel'
hair_colour = 'Brown'

# Prompt user for input and Re-assign these
# name = input('what new name would you like?')

name = input("What do you want to be called? ")
last_name = input("Okay, so what about your last name? ")
species = input("You can change your species too. Just type it out. ")
eye_colour = input("Why not change your eyes and hair too. What colour for your eyes? ")
hair_colour = input("And put your new hair colour here. ")

# Print them back to the user as conversation
# Example: 'Hello Jack! Welcome, your age is 26, your eyes are green and your hair color is black.

print(f"Hello {name.title()} of the {last_name.title()} household. Life must be hard as a {species.lower()}, especially having {eye_colour.lower()} eyes and {hair_colour.lower()} hair.")