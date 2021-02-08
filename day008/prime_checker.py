
def prime_checker(number):
    isPrime = True
    if number <= 1:
        isPrime = False
    else:
        for i in range(2, number):
            if number % i == 0:
                isPrime = False
    if isPrime:
        print("It is a prime number")
    else:
        print("It is not a primer number")

prime_checker(73)
