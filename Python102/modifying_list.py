my_pets = ['Sammy', 'Sheba', 'Henry', 'Annie']
my_pets.append('Katie')

print(my_pets)

del my_pets[4]

# Write a program that has a list of names.
# Add two new names to that list.
# Print the results.
# Write a program that has 5 names in a list.
# Replace the items at index 2 and 4 with "Foo" and "Bar" respectively.
# Write a program that has a list of 5 names.
# Loop through the array printing the item at index 0 and then removing that item from the array until there are no items in the array.
# (hint) This will use a while loop.

new_edition = ['Ralph', 'Ronnie','Ricky', 'Mike']
new_edition += ['Bobby', 'Johnny']
print(new_edition)


new_edition[2] = 'Foo'
new_edition[4] = 'Bar'

index = 0
while index < len(new_edition):
    if new_edition[index] == 0:
        del new_edition[index]
    else:
        print(new_edition[index])  
    index += 1      
