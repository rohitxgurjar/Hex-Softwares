# Rent Calculator
# rent_amount
# food_expense
# electricity_bill
# number_of_people
# Input values
rent_amount = float(input("Enter the rent amount: "))
food_expense = float(input("Enter the food expense: "))
electricity_bill = float(input("Enter the electricity bill: "))
number_of_people = int(input("Enter the number of people: "))

# Calculate total expense
total_expense = rent_amount + food_expense + electricity_bill

# Calculate expense per person
expense_per_person = total_expense / number_of_people
print("\n----- Rent Calculator -----")
print("Total Expense =", total_expense)
print("Expense per Person =", expense_per_person)