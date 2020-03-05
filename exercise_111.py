# mr Miyagi trainee

# make a mr miyagi virtual assistant

# as a user I should be able to speak with mr miyagi and get appropriate response s as I go

# Ask for user input and depending on the response, mr Miyagi will respond.
#
# prompt user for input
# Evaluate each input and print the appropriate responses
# Follow these rules:
#
# every time you ask a question --> Mr. Miyagi responde with
    # --> 'questions are wise, but for now. Wax on, and Wax off!'
# every statement/question must start with Sensei, otherwise:
    # --> 'You are smart, but not wise - address me as Sensei please'
# every time you mention 'block' or 'blocking' --> Mr. Miyagi responde with
    # --> 'Remeber, best block, not to be there..'
# anything else you say:
    # --> 'do not lose focus. Wax on. Wax off.'


# Make it so you keep playing until we say: 'Sensei, I am at peace'
    # --> 'Sometimes, what heart know, head forget'

# your_response = input('(MR.Miyagi)... -.-')

sentence = input("Do you want to talk to Mr Miyagi? ")

while sentence == 'yes' or  sentence == 'y':
    sentence = input("Ok ask him a question then. ")
    if 'Sensei' not in sentence:
        print("You are smart, but not wise - address me as Sensei please")
    elif 'block' in sentence:
        print("Remeber, best block, not to be there..")
    elif '?' in sentence:
        print("Questions are wise, but for now. Wax on, and Wax off!")
    else:
        print("Do not lose focus. Wax on. Wax off.")

    sentence = input("Do you want to talk to Mr Miyagi? ")