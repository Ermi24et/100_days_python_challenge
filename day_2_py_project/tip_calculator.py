
print("Welcome to the tip calculator!")
total_bil = float(input("What was the total bil: $"))
tip_in_percent = float(input("what percent tip would you like to give? 10, 12, or 15: "))
total_people = int(input("how many people to split the bill: "))

total_bil_with_tip = total_bil * (tip_in_percent / 100) + total_bil
bil_later = total_bil_with_tip / total_people
rounded_res = round(bil_later, 2)

print(f"each person should pay: {rounded_res}")
