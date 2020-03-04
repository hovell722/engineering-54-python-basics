# For Loops

# Syntax

# for item in iterable:
    # block of code

cool_cars = ['Skoda Felicia Fun', 'Fiat Abarth the old one', 'Toyota Corola', 'Fiat Panda 4x4', 'Fiat Multpla']

count = 1
for car in cool_cars:
    print(count, '-', car)
    count += 1

# For Loops for Dictionaries

boris_dict = {
    'name': 'Boris',
    'surname': 'Johnson',
    'phone': '07284624634',
    'address': '10 Downing Street'
}

for key in boris_dict:
    print(key)
    # I want each individual values
    # For this I need, dictionary + key
    print(boris_dict[key])

# print(boris_dict['phone'])

# for key in boris_dict:
    # print(boris_dict[key])
    