counter = 1 
while counter <= 10:
    print(counter)
    counter += 1
counter = 10
while counter >= 1:
    print(counter)
    counter -= 1

# Create a program that has a variable named username and another variabled named password with values of your choice.
# Prompt the user for a username and then a password.
# If the both match continue on with the program and give a welcome message.
# If not it prompts the user for the username and password until they get it correct.
# (bonus) have a limited amount of attempts and if they reach the limit it tells the user and exits the program.

username = "Robby"
password = "Charlotteboy06"


attempts = 0
while attempts < 4:
    attempts += 1
    user_prompt = input("\nWhat is your username: ")
    pass_prompt = input("\nWhat is your password? ")
    if user_prompt == 'quit' or pass_prompt == 'quit' :
        break
    if user_prompt == username and pass_prompt == password:
        print("Welcome!")
        break
    elif user_prompt != username and pass_prompt == password:
        print("Wrong Username")

    elif user_prompt == username and pass_prompt != password:
        print("Wrong password")   


