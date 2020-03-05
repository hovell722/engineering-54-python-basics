# Dictionary basics :D
#1 - Define a dictionary call story1, it should have the followign keys:
        # start, middle and end
#2 - Print the entire dictionary
#3 - Print the type of your dictionary
#4 - Print only the keys
#5 - print only the values
#6 - print the individual values using the keys (individually, lots of printi commands)
#7 - Now let's add a new key:value pair.
    # 'hero': yourSuperHero

# 1
story1 = {
    'start' : 'Baby shoes.',
    'middle' : 'For sale.',
    'end' : 'Never worn.'
}

# 2
print(story1)

# 3
print(type(story1))

# 4
print(story1.keys())

# 5
print(story1.values())

# 6
print(story1['start'])
print(story1['middle'])
print(story1['end'])

# 7
story1['author'] = 'Ernest Hemingway'
story1['soundtrack'] = 'Idles'
