print("Welcome to the tip calculator!")
total_bill = float(input("What was the total bill? $"))
tip = (float(input("How much tip would you like to give? 10, 12, or 15? ")) + 100) / 100
nb_ppl = float(input("How many people to split the bill? "))
result = round(((total_bill * tip) / nb_ppl), 2)
print("Each person should pay: $" + str(result))
