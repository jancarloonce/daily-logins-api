# checks whether a given n is a prime

def is_prime(n):
    if n <= 1:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

# finds the product of coefficients and returns it
def solution():
    max_count = 0
    product = 0

    for a in range(-999, 1000):
        for b in range(-1000, 1001):
            n = 0
            while is_prime(abs(n * n + a * n + b)):
                n += 1
            if n > max_count:
                max_count = n
                product = a * b

    return product

print(solution())