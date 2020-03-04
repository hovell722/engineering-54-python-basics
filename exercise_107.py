# SIMPLEST - Restaurant Waiter Helper

# User Stories
#1
# AS a User I want to be able to see the menu in a formated way, so that I can order my meal.

#2
# AS a User I want to be able to order 3 times, and have my responses added to a list so they aren't forgotten

#3
# As a user, I want to have my order read back to me in formated way so I know what I ordered.

# DOD
# its own project on your laptop and Github
# be git tracked
# have 5 commits mininum!
# has documentation
# follows best practices

# starter code
menu = ['falafel', 'HuMMus', 'coUScous', 'Bacalhau a Bras']
food_order = []


menu[0] = menu[0].upper()
menu[1] = menu[1].upper()
menu[2] = menu[2].upper()
menu[3] = menu[3].upper()

print(f"Today on the menu we have {menu[0]}, {menu[1]}, {menu[2]} and {menu[3]}.")
order_1 = input("Please tell me 1 thing you would like. ")
order_2 = input("Give me another food order. ")
order_3 = input("And your third dish? ")

food_order.extend([order_1.upper(), order_2.upper(), order_3.upper()])
print(f"You have ordered {food_order[0]}, {food_order[1]} and {food_order[2]}.")



# I need to print each item from the list
# print(menu[0])
# before I print I need to make them all capitalized
#  print everything