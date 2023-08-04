print("welcome to the pizza delivery")
size = input("what size pizza do you want? S, M, L: ")
add_pepperoni = input("do you want peperroni? Y, N: ")
extra_cheese = input("do you want extra cheese? Y, N: ")
bil = 0

if size == "S":
    bil = 15
    if add_pepperoni == "Y":
        bil += 2
elif size == "M":
    bil = 20
    if add_pepperoni == "Y":
        bil += 3
elif size == "L":
    bil = 25
    if add_pepperoni == "Y":
        bil += 3
else:
    print("Invalid Letter!")
if extra_cheese == "Y":
    bil += 1
print(f"your final bil is ${bil}")