number = int(raw_input("Enter a number: "))

def is_prime(n):
    for i in range(2, n):
        if i % n == 0:
            return False
    return True
    
factors = []

for i in range(2, number +1):
    while number % i == 0:
        if is_prime(i):
            factors.append(i)
            number /= i

print factors