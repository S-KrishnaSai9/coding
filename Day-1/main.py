
print("Welcome to the Band Name Generator.")

city = ""
pet_name = ""

while True:
    print("What's the name of the city you grew up in?")
    city = input("> ")
    if city == "":
        print("You haven't entered anything. Please try again.")
    else:
        break

while True:
    print("What's your pet's name?")
    pet_name = input("> ")
    if pet_name == "":
        print("You haven't entered anything. Please try again.")
    else:
        break
print(f"Your band name could be {city} {pet_name}.")
