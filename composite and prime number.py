def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
numbers = [4, 54, 29, 71, 59, 98, 23]
prime_count = 0
composite_count = 0
for num in numbers:
    if num > 1:
        if is_prime(num):
            prime_count += 1
        else:
            composite_count += 1
print("Composite numbers =", composite_count)
print("Prime numbers =", prime_count)
