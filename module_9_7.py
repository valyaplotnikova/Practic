"""
Результат консоли:
Простое
11
"""


def is_prime(func):
    def wrapper(*args):
        res = func(*args)
        count = 0
        for _ in range(2, res):
            if res % _ == 0:
                count += 1
        if count == 0:
            print("Простое")
        else:
            print("Составное")
        return res
    return wrapper


@is_prime
def sum_three(*args):
    return sum(args)


result = sum_three(2, 3, 6)
print(result)
