import random
print("welcome to the python password genarator!")
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
nums = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
syms = ['!', '@', '#', '$', '^', '&', '*', '(', ')', '+']
accepted_letters = int(input("how many letters do you like to have?\n"))
accepted_symbols = int(input("how many symbols do you want to have?\n"))
accepted_numbers = int(input("how many numbers do want to have?\n"))
final_string = []
for i in range(1, accepted_letters + 1):
    final_string += random.choice(letters)
for i in range(1, accepted_numbers + 1):
    final_string += random.choice(nums)
for i in range(1, accepted_symbols + 1):
    final_string += random.choice(syms)
random.shuffle(final_string)
password = ""
for i in final_string:
    password += i
print(f"your password is: {password}  keep your pw safe!")