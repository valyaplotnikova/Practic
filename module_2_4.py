numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
not_primes = []

for n in numbers:
    for _ in range(2, n):
        if n % _ == 0:
            not_primes.append(n)
            break
primes = [i for i in numbers if (i not in not_primes and i != 1)]

print(f"Primes: {primes}")
print(f"Not Primes: {not_primes}")
