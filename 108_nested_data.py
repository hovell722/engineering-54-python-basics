# Nested data structures

crazy_landl_1 = {
    'name' : 'Boris',
    'phone' : '07294837283',
    'address of rent' : '10 Chelsea Road',
    'age' : 56
}

crazy_landl_2 = {
    'name' : 'James',
    'phone' : '07528385212',
    'address of rent' : '53 Norman Road',
    'age' : 24
}

nested_dictionary = {'Boris' : crazy_landl_1,
                     'James' : crazy_landl_2
                     }

print(nested_dictionary)

for key in nested_dictionary:
    print(key)
    for nest_key in nested_dictionary[key]:
        print(nest_key, nested_dictionary[key][nest_key])

nest_list = [[1, 2, 3], [4, 5, 6]]

print(nest_list[0])
print(nest_list[1])
print(nest_list[1][0])


for data in nest_list:
    print(data)
    for num in data:
        print(num * 20)