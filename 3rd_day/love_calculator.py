print("welcome to the love calculator!")
name1 = input("Enter your name: ")
name2 = input("Enter your name: ")
upper_name1 = name1.upper()
upper_name2 = name2.upper()
name = upper_name1 + upper_name2
L = name.count("L")
Ov = name.count("O")
V = name.count("V")
E = name.count("E")
T = name.count("T")
R = name.count("R")
U = name.count("U")
true = T + R + U + E
love = L + Ov + V + E
joined_str = str(true) + str(love)
joined_int = int(joined_str)
if 10 > joined_int > 90:
    print(f"your score is {joined_int}, you go together like coke and mentos.")
elif 40 < joined_int < 50:
    print(f"your score is {joined_int}, you are alright together.")
else:
    print(f"your score is {joined_int}")
