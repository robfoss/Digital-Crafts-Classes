def my_func():
    print('I am a function.')

my_func()

# Create a program that defines function that prints a message with your name.
# Call the function 3x.

def name(name):
    print(name)

name('Rob Foss')
name('Rob Foss')
name('Rob Foss')

# Creat a program that has a function that will multiply two numbers together and print out the results.

# Make the program properly handle an exception if something besides a number is passed as an argument.
# Have it print out 3 different sets of numbers
# Create a program that has a function that will accept 3 arguments as title, genre, year and then print out the values in list format.

#     1. Title : Star Wars - A new Hope
#     2. Genre : Sci-Fi
#     3. Year  : 1977
# Create a program that does the same thing as above, but the function only accepts a single argument to get the same results.
# (hint) - You will need to use a datatype other than a string in the argument.

def multiply(a, b):
    a = int(a)
    b = int(b)
    print(a * b)
multiply(3, 3)    
multiply(4, 4)
multiply(5, 5)

def movies(title, genre, year):
    print(f"1. Title: {title.title()}\n2. Genre: {genre.title()}\n3. Year: {year}")
movies('friday', 'comedy', 1995)    

def movies_again(obj):
    idx = 1
    for movie in obj:
        print(f'{idx}. {movie}: {obj[movie]}')
        idx += 1

friday = {
    'Title': 'Friday',
    'Genre': 'Comedy',
    'Year': '1995'
}        

movies_again(friday)


# Write a program that has a function with two parameters.

# return the concatinated value of the two parameters.
# print the results.
# Write a program that has a function named total_count that expects a list of strings as it argument when the function is called.

# Have the returned value be a dictionary with the keys 'list_length' and 'total_chars'.
# The list_length value needs to be the length of the list and the total_chars needs to be the total count of characters of all of the items in the array.
# Call the function 3 times with 3 different lists.
# (hint) len is usable on lists and strings.
#     #expected output
#     totals = total_count(['I', 'Am', 'Awesome'])
#     print(totals) #{list_length:3, total_chars:10}

def my_function(param1, param2):
    return f'{param1} {param2}'

print(my_function('Rob', 'Foss'))




