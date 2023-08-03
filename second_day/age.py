print("Welcome to the teller of your remaining ages in days")
age = int(input("Enter your current age: "))
remaining_age = 90 - age
remaining_days = remaining_age * 365
remaining_weeks = remaining_age * 52
remaining_months = remaining_age * 12
print(f"you have {remaining_days} days, and {remaining_weeks} weeks, and {remaining_months} months left")
