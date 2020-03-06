#
#  Don't need to do this exercise!


# Mega fizz buzz exercise
# this exercise has 4 versions

# Boring Buzz
# The point of the game is to count up to a number and whenever we get multiples of 3 you will respond with 'boring' and multiples of 5 you'll respond with 'buzz'.
# multiples of 3 and 5 youll respond with 'boringbuzz'
# do this exercise with while loop and if functions.

#specs:
# multiples of 3 -- > boring
# multiples of 5 -- > buzz
# multiples of 3 and 5 --> boringbuzz


# then do this functionally

number = ' '

while number != 'exit':
    number = input("Give me a number: ")
    if number.isdigit():
        number = int(number)
        for n in range(1, number + 1):
            if (n % 5 == 0) and (n % 3 == 0):
                print('boringbuzz')
            elif n % 3 == 0:
                print('boring')
            elif n % 5 == 0:
                print('buzz')
            else:
                print(n)
    elif number == 'exit':
        print('Goodbye!')
        break
    else:
        print('Not a valid number!')


