# While Loops

# Syntax

# while <condition>:
    # run block of code
    # if <condition>:
        # break

# counter = 0

# while counter <= 10:
#     print(counter)
#     print('this is cool')
#     counter += 1


# reserved words
# break - used to break the while loop
# continue - skips to the next iteration without running the following code/blocks

user_input = input('you want to play? ')

while user_input == 'yes'or user_input == 'y':
    random_num = 10
    print('welcome to our random game')
    user_input = input('what is your guess? ')
    if int(user_input) == random_num:
        print('WELL DONE! WELL DONE!')
    else:
        print("sorry you're not a winner")
    user_input = input('play again? ')


