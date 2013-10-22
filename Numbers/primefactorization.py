number = int(raw_input("Enter a number: "))

#check if a number is prime (naive algorithm)
def is_prime(n):
    sum = 0
    for x in range(1, n):
        if n%x == 0:
            sum = sum + 1
    if sum < 2:
        return True
    else:
        return False

factors = []