base_bill = ""
percentage = ""
people = ""

print("Welcome to the tip calculator.")

while True:
    print("What was the total bill?")
    base_bill = input("> $")
    try:
        float(base_bill)
        if float(base_bill) < 0:
            print("The bill can't be negative. Please enter a valid amount.")
        else:
            break
    except ValueError:
        print("Please enter a valid amount.")

while True:
    print("What percentage tip would you like to give? 10, 12, or 15?")
    percentage = input("> ")
    choices_list = ["10", "12", "15"]
    if percentage not in choices_list:
        print("Please enter 10, 12 or 15.")
    else:
        break

while True:
    print("How many people to split the bill?")
    people = input("> ")
    if not people.isdigit() or people == "0":
        print("Please enter a valid number of people (1,2,3, etc.)")
    else:
        break

total_bill = float(base_bill) * (1 + int(percentage) / 100)
split_bill = round(total_bill / int(people), 2)
print(f"Each person should pay: ${split_bill}")
