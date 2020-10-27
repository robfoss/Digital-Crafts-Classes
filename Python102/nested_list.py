# people = [
#     ['Rob', 'Foss', 33],
#     ['Margaret', 'Foss', 31]
# ]

# first_person = people[0]
# first_person_age = people[0][2]


# for person in people:
#     print("First", "Last", 'Age')
#     for attribute in person:
#         print(attribute)

# Write a program that has a list of shopping lists that where each list is for a different food group.
# Print each full list on a seperate line.
# ['Corn','Potatoes','Tomatoes']
# ['milk','eggs','cheese','yogurt']
# ['frozen pizza','popsicle']
# Using the code from the previous exercise, have each grouping have a title with the number in the title and each item of the list have a number in front of the item.
# (bonus) Have each of the titles of the main grouping be in a seperate list that gives the name to the heading.
# 1. Veggies
#     1. Corn
#     2. Potatoes
#     3. Tomatoes
# 2. Cold Items
#     1. milk
#     2. eggs
# ...etc        


count = 1
index = 1
list_of_list = [['milk', 'eggs', 'cheese'], ['shirts', 'shoes', 'pants']]

for lists in list_of_list:
    index += 1
    print(f'{index} {lists}')

    





