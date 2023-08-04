print("welcome to the updated version of BMI")
height = float(input("Enter your height in m: "))
weight = float(input("Enter your weight in KG: "))
result = weight / (height * height)
rounded_result = round(result)
if result < 18.5:
    print(f"your BMI is {rounded_result}, and you are underweight")
elif result < 25:
    print(f"your BMI is {rounded_result}, and you are in a normal weight")
elif result < 30:
    print(f"your BMI is {rounded_result}, and you are in a overweight")
elif result < 35:
    print(f"your BMI is {rounded_result}, and you are in a obese")
else:
    print(f"your BMI is {rounded_result}, and you are in a clinically obese")