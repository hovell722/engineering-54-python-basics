
# Write a bizz and zzuu game ##project

# as a user I should be able prompted for a number, as the program will print all the number up to and inclusing said number while following the constraints / specs. (bizz and buzz for multiples or 3 and 5)

# As a user I should be able to keep giving the program different numbers and it will calculate appropriately until you use the key word: 'penpinapplespen'


# write a program that take a number
# prints back each individual number, but
    # if it is a multiple of 3 it returns bizz
    # if a multiple of 5 it return zzuu
    # if a multiple of 3 and 5 it return bizzzzuu

# number = input("Please put in a number. ")

# while type(number) == type('a'):
#
# # while not input = penpineapple
#     # if input is digit
#         # play the game
#     # else
#         # invalid input
#
#
#     if number == "penpinapplespen":
#         break
#     elif int(number) % 3 == 0 and int(number) % 5 == 0:
#         print("bizzzzuu")
#     elif int(number) % 3 == 0:
#         print("bizz")
#     elif int(number) % 5 == 0:
#         print("zzuu")
#     else:
#         print("Isn't a multiple of 3 or 5")
#     number = input("Please out in a number. ")

number = ' '

while number != 'penpinapplespen':
    number = input('Guess a number: ')
    if number.isdigit():
        number = int(number)
        for n in range(1, number + 1):
            if (n % 3 == 0) and (n % 5 == 0):
                print("bizzzzuu")
            elif n % 3 == 0:
                print("bizz")
            elif n % 5 == 0:
                print("zzuu")
            else:
                print(n)
    elif number == "penpinapplespen":
        print("goodbye")
        break
    else:
        print("not number")

