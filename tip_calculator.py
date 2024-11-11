# Simple string tip calculator to complete day 2 of 100
# focusing on data types, f-strings

print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))

tip_add = (1 + tip / 100)
split_bill = bill / people

final_bill = split_bill * tip_add
print(f"Each person should pay ${final_bill:.2f}")





