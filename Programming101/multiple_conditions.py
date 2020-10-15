name = input("What is your name?\n")

num = len(name)

if num > 3 and num < 15: # and operator both statement need to be true
    if num == 4:
        print("Perfect Length")
    else:
        print("It's an ok length.")    

    print(f"Welcome {name}!")    

else:
    print(f"{num} is not a good number of characters.")    

if num > 3 or num < 15: # or operator, 1 statement needs to be true 
    print("This is valid")    