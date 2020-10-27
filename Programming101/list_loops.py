# List are a ordered group of values... like an array.
# Index is the number representation of the item in the list - index always start a 0

# todos = []
# new_todo = input("What do you need to do? ")
# while len(new_todo) > 0:
#     todos.append(new_todo)

#     # Print the current list of to-do items
#     print("To do:")
#     print("====================")
#     count = 1
#     for todo in todos:
#         print("%d: %s" % (count, todo))
#         count += 1

#     # Prompt the user again
#     print("\n")
#     new_todo = input("What do you need to do? ")

# print("Have a nice day!")



list = [1, 2, 3, 'car', True, None]

name = 'Rob'
age = 31
married = False

my_new_list = [name, age, married]
print(my_new_list)

size = 5
board = []

for i in range(size):
    board.append([])

    for j in range(size):
        board[i].append(f"{[i]} {[j]}")

print(board) 

my_family = ['Erikka', 'Pearl', 'Erick', 'Momma', 'Skylar', 'Akira', 'Pheonix']
print(my_family[3])

my_grandmother = my_family[1]

print(my_grandmother)