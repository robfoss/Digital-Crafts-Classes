my_number = 7

user_answer = int(input("Guess my number: \n"))

if user_answer == my_number:
    print("Wow correct!")
elif user_answer < my_number:
    print("Too low.")    
else:
    print("Too high.")    
