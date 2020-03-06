# number = ' '
#
# while number != 'exit':
#     number = input("Give me a number: ")
#     if number.isdigit():
#         number = int(number)
#         for n in range(1, number + 1):
#             if (n % 5 == 0) and (n % 3 == 0):
#                 print('boringbuzz')
#             elif n % 3 == 0:
#                 print('boring')
#             elif n % 5 == 0:
#                 print('buzz')
#             else:
#                 print(n)
#     elif number == 'exit':
#         print('Goodbye!')
#         break
#     else:
#         print('Not a valid number!')


def num_mod_num(num1, num2):
    return num1 % num2 == 0


def boringbuzz_if(n):
    if num_mod_num(n, 3) and num_mod_num(n, 5):
        return 'boringbuzz'
    elif num_mod_num(n, 3):
        return 'boring'
    elif num_mod_num(n, 5):
        return 'buzz'
    else:
        return n


def boringbuzz_for(number):
    print("hello")
    my_list = []
    # make a list   my_list = []
    # add the number into the list my_list.append(n)
    # return the list
    for n in range(1, number + 1):
        my_list.append(boringbuzz_if(n))
    return my_list

def my_funct(list):
    for thing in list:
        boringbuzz_for(5)


