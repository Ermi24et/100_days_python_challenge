def prime_checker(number):
    check_int = True
    for i in range(2, number - 1):
            if number % i == 0:
                check_int = False
    if check_int:
        print("It's a prime number.")
    else:
        print("It's not a prime number.")


n = int(input("Check this number: "))
prime_checker(number=n)
