print("welcome to the odd or even checker!")
num = int(input("Enter the number you want to check: "))
remainder = num % 2
if remainder == 0:
    print(f"{num} is even")
else:
    print(f"{num} is odd")
