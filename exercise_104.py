from datetime import date

# name, last_name, species, eye_color, hair_color, age
# name = 'Lana'

name = 'James'
last_name = 'Hovell'
species = 'Human'
eye_colour = 'Hazel'
hair_colour = 'Brown'
age = '24'

# Prompt user for input and Re-assign these
# name = input('what new name would you like?')

name = input("What do you want to be called? ")
last_name = input("Okay, so what about your last name? ")
species = input("You can change your species too. Just type it out. ")
eye_colour = input("Why not change your eyes and hair too. What colour for your eyes? ")
hair_colour = input("And put your new hair colour here. ")
age = int(input("Finally, how old do you want to be? "))

## Calculate year of birth
# import time
# calculate the difference

today = date.today()
year_of_birth = today.year - age

# Print them back to the user as conversation including the year they were born!
# Example: 'Hello Jack! Welcome, your age is 26, your eyes are green and your hair color is black.
# print something like: 'You said you we're 28 hence you were born in 1991!'

print(f"Wagwan {name.title()} {last_name.title()}, man be {age} so man was born in {year_of_birth} unless man ")
print(f"hasn't had his bday this year, then man was born in {year_of_birth - 1}.")
print(f"So recognisable with your {eye_colour.lower()} eyes and {hair_colour.lower()} hair. Such a strange looking {species.lower()}.")

# Section 2 - Calculate the Age difference!
# ask user for their name and age -- store these in variables
# ask user for their Mothers name and age

mum_name = input("What is your mothers name? ")
mum_age = int(input("How old is your mum? "))
mum_yob = today.year - mum_age
age_difference = mum_age - age

# calculate the difference and year of birth for each
# print out these formated. something along the lines of:
# your name is <name>, and you are <age> born on the year of <y_birth>. This is <difference_y> later than <mom_name> who was on on <y_birth_mon>

print(f"Your name is {name.title()}, and you are {age} born on the year of {year_of_birth}. This is {age_difference}")
print(f"later than {mum_name.title()} who was born on {mum_yob}")