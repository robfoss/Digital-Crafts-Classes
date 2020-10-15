pet_name = input("What is your pets name?\n").title()
length = len(pet_name)

if length < 3:
    print("That too short.")
if length > 3:
    print(f"Awww sweet {pet_name}")
    if pet_name == "Shadow":
        print("El Gato Diablo!")
    if pet_name == "Daisy" :
        print("Good Dog!") 
    else:
        print("Awesome name!")      


