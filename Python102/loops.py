# #while loops
# my_family = ['Momma', 'Pearl', 'Erikka']
# index = 0
# while index < len(my_family):
#     print(my_family[index])
#     index += 1

# #for loops
# idx = 1
# for idx, member in enumerate(my_family):
#     print(idx, member)    

# for member in my_family:
#     print(member)

# Using a while loop create a program that prints the values of your favorite movie stars.

# have a number in front of the printed name.
# Using a for loop, re-do the above exercise.

# (hint) you still need to create a variable that is incrimented.
# Create a program that will add the values of a list of numbers, and then print out the results.

# (hint) You will need to create a variable to hold the current value.
# Repeat with several different lists of numbers of different lengths.

favorite_stars = ['George Clooney', 'Will Smith', 'Halle Berry', 'Tom Hanks', 'Denzel Washington', 'Jennifer Lopez']
# index = 0
# counter = 1
# while index < len(favorite_stars):
#     print(f'{counter}. {favorite_stars[index]}')
#     index += 1
#     counter += 1

print('\n')

counter = 1
for star in favorite_stars:
    print(f'{counter}. {star}') 
    counter += 1  

nums = [1, 2, 3, 4, 5, 7, 7, 7, 9]
current_value = 0

for i in nums:
    current_value += i
print(current_value)    

