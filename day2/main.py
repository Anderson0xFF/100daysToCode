print("Welcome to the tip calculator.")
total = float(input("What was the total bill? $"))
percent = int(input("What percentage tip would you like to give? 10%, 12%, or 15%? "))
people = int(input("How many people to split the bill? "))

total += ((percent * total) / 100)
per_person = round(total / people, 2)
print(f"Each person should pay: ${per_person}") 