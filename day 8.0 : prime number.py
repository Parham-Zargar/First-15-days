def prime_checker(number):
    prime = True
    for i in range(2, number):
        if number % i == 0:
            prime = False
    if prime:
        print("It's prime")
    else:
        print("It's not prime")


n = int(input("check this number: "))
prime_checker(number=n)