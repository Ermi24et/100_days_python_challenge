import random
test_seed = int(input("craete a seed number: "))
random.seed(test_seed)
names = input("provide all the names: ")
separator = names.split(", ")
length = len(separator)
select = random.randint(1, length - 1)
print(f"{separator[select]}, is going to pay the bill today")
