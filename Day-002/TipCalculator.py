print('Welcome to the tip calculator!')
total_bill = float(input('What was the total bill? rs/- '))
tip_percentage = int(input('How much tip would you like to give? 10, 12, or 15? '))
no_of_people = int(input('How many people to split the bill? '))
tip_amount = total_bill * (tip_percentage / 100)
total_amount = total_bill + tip_amount
amount_per_person = total_amount / no_of_people
print(f"Each person should pay: rs/- {amount_per_person:.2f}")