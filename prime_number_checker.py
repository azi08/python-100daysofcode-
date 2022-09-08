
def prime_checker(number):
    
    factors = []

    for i in range(1,number+1):
        if number % i == 0:
            factors.append(i)

    if len(factors) > 2:
        print("It's not a prime number.")
    else:
        print("It's a prime number.")

###Other Solution#######

def prime_checker(number):

    factors = [i for i in range(2,number) if number % i == 0]

    if len(factors) > 0:
        print("It's not a prime number.")
    else:
        print("It's a prime number.")

n = int(input("Check this number: "))
prime_checker(number=n)
