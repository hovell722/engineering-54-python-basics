# If Functions

# Syntax

# if <condition>:
    # block of code that runs if condition return True
# elif <condition>:
    # block of code that runs if condition return True
# else:
    # block of code that runs when ALL other conditions are False


# Notes:
# if functions will exit once a condition becomes true
# build your if function with the most specific thing at the top

weather = 'sunny'

if weather == 'rainy':
    print('take your umbrella')
elif weather == 'sunny':
    print('nice, take some shades B)')
else:
    print("Didn't quite catch that, can you please repeat")