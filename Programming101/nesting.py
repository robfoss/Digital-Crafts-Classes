name = input("What is your name?\n")
if len(name) > 3:
    print("Your name is long enough.")

    if len(name) > 15:
        print("That is way too long.")
    else:
        print(f"Welcome {name}")    