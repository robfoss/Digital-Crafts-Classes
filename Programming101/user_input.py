name = input("What is your name?\n")
age = input("How old are you?\n")

# age variable must be converted to integer. all numbers from input function must be converted to integer w/ int().
if int(age) >= 21:
    print("Grab a Beer?")

print(f"Nice to meet you {name.title()}!")

