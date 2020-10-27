# Create a program that has a list of at least 3 of your favorited foods in order and assign that list to a variable named "favorite_foods".

# print out the value of your favorite food by accessing by it's index.
# print out the last item on the list as well.
# Create a program that contains a list of 4 different "things" around you.

# Print out the each item on a new line with the number of it's index in front of the item.
# 0. Coffee Cup
# 1. Speaker
# 2. Monitor
# 3. Keyboard

# Using the code from exercise 2, prompt the user for which item the user thinks is the most interesting. Tell the user to use numbers to pick. (IE 0-3).

# When the user has entered the value print out the selection that the user chose with some sort of pithy message associated with the choice.
#     "You chose Coffee Cup, You must like coffee!"


favorite_foods = ['seafood paella', 'spinach', 'salmon']
first = favorite_foods[0]
second = favorite_foods[1]
third = favorite_foods[2]
print(f'My favorite foods are {first}, {second}, and {third}.')
print('\n')


things_around_me = ['laptop', 'bookbag', 'energy', 'monitors']
count = 1
for things in things_around_me:
    print(f'{count}. {things}\n')
    count += 1

print('\n')

user_opinion = int(input("Which item do you think is interesting? Pick a number between 0 and 3\n"))
