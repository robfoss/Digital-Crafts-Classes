first_name = 'rob'
last_name = 'foss'

print(f"{first_name.title()} {last_name.title()}")

haiku = "This is my\nHaiku, that does not\nMake sense."
print(haiku)

full_name = f"{first_name.title()} {last_name.title()}"
today = 'Tuesday'
emotion = 'motivated'

print(f"""
Hello {full_name},
I hope that your {today} is going well.
I'm personally really {emotion}
""")

print("Hello " + full_name +"," + "\nI hope that your " + today + " is going well." + "\nI'm personallhy really " + emotion + ".") 