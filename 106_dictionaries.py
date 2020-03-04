# Dictionaries
# Work with key and value pairs.
# Work like a real dictionary, you just look up the information for the specific key
# The big difference with list is they are organised with index and here we use keys

# We just made a list of cringe_land_l, but we need more information. Like their phone numbers and address.

# Syntax
dict_variable_name = {'key': 'value'}

boris_dict = {
    'name': 'Boris',
    'surname': 'Johnson',
    'phone': '07284624634',
    'address': '10 Downing Street'
}

print(boris_dict)
print(type(boris_dict))

# Access one key value pair
# Follow the same principle of a list, but, use keys not indexes

print(boris_dict['name'])

last_name = boris_dict['surname']
print(last_name)

# Change the value ov one key value pair

boris_dict['phone'] = '+74902341254'
print(boris_dict['phone'])

# Assign a new key value pair
# print(boris_dict)

boris_dict['home phone'] = '+447 394838294'
print(boris_dict)

boris_dict['number budgets passed'] = 0
print(boris_dict)

#The following 2 lines do the same thing - increase the orginal by 1
boris_dict['number budgets passed'] = boris_dict['number budgets passed'] + 1
boris_dict['number budgets passed'] += 1
print(boris_dict)

# Get all the keys

print(boris_dict.keys())

# Get all the values

print(boris_dict.values())

# Nested Structures