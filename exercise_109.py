age = 12
driver_license = True


# - You can vote and drivre
# - You can vote
# - You can driver
# - you can't leagally drink but your mates/uncles might have your back (bigger 16)
# - Your too young, go back to school!


 #  as a user I should be able to keep being prompted for input until I say 'exit'


# print("If you want to end this at any point type 'exit' as your age and anything in the driving license.")
# age = input("Enter your age: ")
# driver_license = input("Can you drive? ")
#
#
# if driver_license == "yes" or driver_license == "y":
#     driver_license = True
# else:
#     driver_license = False
#
# while (driver_license == True) or (driver_license == False):
#
#     if 'exit' in age:
#         print('goodbye!')
#         break
#     elif driver_license and int(age) >= 18:
#         print("Well done, now you can do adult things!")
#     elif not driver_license and int(age) >= 18:
#         print("Now you just need to learn to drive!")
#     elif driver_license and int(age) == 17:
#         print("Well at least it's not your fault Boris is in charge!")
#     elif not driver_license and int(age) == 17:
#         print("Go and learn to drive, then come back. You might be old enough to vote then.")
#     elif driver_license and int(age) < 17:
#         print("You can't have a driving license at your age. Please don't lie again.")
#     else:
#         print("You've got to wait a some time kiddo. Come back when you're older.")
#
#
#     print("Lets see if your answers change.")
#
#     age = input("What is your age now? ")
#     driver_license = input("Can you drive now? ")
#
#     if driver_license == "yes" or driver_license == "y":
#         driver_license = True
#     else:
#         driver_license = False

user_input = ' '
while user_input != 'exit':
    user_input = input("How old are you? ")
    if user_input.isdigit():


