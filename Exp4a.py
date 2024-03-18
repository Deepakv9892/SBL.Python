def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

num = int(input('Please Enter the Number'))
if is_prime(num):
    print(num, "is a prime number")
else:
    print(num, "is not a prime number")
