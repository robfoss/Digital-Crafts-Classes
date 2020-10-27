
# good = 20
# fair = 15
# bad = 10
# tip = 0

# total_bill = int(input("How much is the bill?\n"))
# service_rate = input("Would you rate the service Good, Fair or Bad?\n ")
# if service_rate == 'good':
#     tip = int(good)
# elif service_rate == 'fair':
#     tip = int(fair)
# elif service_rate == 'bad':
#     tip = int(bad)
# else:
#     print("Please choose between good, fair, or bad.")        

# tip_percentage = float(tip / 100)
# final_total = (total_bill * tip_percentage) + total_bill
 
# print(f"Based on the level of service your tip should be {tip}%.")
# print(f"With tip your total bill comes to {final_total}!")

# good = 20
# fair = 15
# bad = 10
# tip = 0
    
# total_bill = int(input("How much is the bill?\n"))
# split = input("Will you be splitting the bill?\n")
# if split == 'yes':
#     splitby = int(input("How many ways are you splitting the bill?\n"))
#     service_rate = input("Would you rate the service Good, Fair or Bad?\n")
#     if service_rate == 'good':
#         tip = int(good)
#     elif service_rate == 'fair':
#         tip = int(fair)
#     elif service_rate == 'bad':
#         tip = int(bad)
#     else:
#         print("Please choose between good, fair, or bad.")        
#     tip_percentage = float(tip / 100)
#     final_total = (total_bill * tip_percentage) + total_bill
#     split_total = final_total / splitby
#     print(f"Based on the level of service your tip should be {tip}%.")
#     print(f"With tip your total bill comes to {split_total} each!")
# else:
#     service_rate = input("Would you rate the service Good, Fair or Bad?\n")
#     if service_rate == 'good':
#         tip = int(good)
#     elif service_rate == 'fair':
#         tip = int(fair)
#     elif service_rate == 'bad':
#         tip = int(bad)
#     if service_rate == 'good':
#         tip = int(good)
#     elif service_rate == 'fair':
#         tip = int(fair)
#     elif service_rate == 'bad':
#         tip = int(bad)
#     else:
#         print("Please choose between good, fair, or bad.")        
#     tip_percentage = float(tip / 100)
#     final_total = (total_bill * tip_percentage) + total_bill
#     print(f"Based on the level of service your tip should be {tip}%.")
#     print(f"With tip your total bill comes to {final_total}!")


# Write a program that will prompt you for how many coins you want. Initially you have no coins. 
# It will ask you if you want a coin? If you type "yes", it will give you one coin, and print out the current tally. 
# If you type no, it will stop the program. Example run:

# current_coins = 0
# desire_coins = True

# while desire_coins:
#     coins = input("Would you like a coin? Yes or No?\n")
#     if coins == "yes":
#         current_coins += 1
#         print(current_coins)
#     else:
#         print("Goodbye!")
#         break

# print("Hollow Box Star Pattern")

# i = 1
# while(i <= rows):
#     j = 1;
#     while(j <= columns ):
#         if(i == 1 or i == rows or j == 1 or j == columns):
#             print('*', end = '  ')
#         else:
#             print(' ', end = '  ')
#         j = j + 1
#     i = i + 1
#     print()




# # Ask the use for input and turn it into an integer.
# width = int(input('Enter a width: '))
# height = int(input('Enter a height: '))
# # # Set up start of loop by instantiating variable i at 1
# # i = 1
# # # Loop is going from 1 to the height of the box.
# # while (i < (height+1)):
# #     # If we are at the top or bottom of box, we're going to print as many * as the width is.
# #     if (i == 1 or i == height):
# #         print("*" * width)
# #     # If we are in the middle of the box we're going to print a * then print " " then print another * for the borders.    
# #     else:
# #         print('*' + (' ' * (width-2)) + '*')
# #     # increment i by 1    
# #     i+=1

# for i in range(1, height + 1):
#     if (i == 1 or i == height):
#         print("*" * width)  
#     else:
#         print('*' + (' ' *  (width - 2)) + '*' )     


# number = int(input("enter the number of rows: "))
# row = 0
# while row < number:
#     blanks = number - row - 1
#     while blanks > 0:
#         print(end = ' ')
#         blanks = blanks - 1
#     star = row + 1
#     while star > 0:
#         print("*", end = ' ')
#         star = star - 1
#     row = row + 1
#     print() 

# num = 1
# while num <= 10:
#     i = 1
#     while i <= 10:
#         product = num * i
#         print(f"{num} * {i} = {product}\n")
#         i += 1
#     num += 1
#     print()    

