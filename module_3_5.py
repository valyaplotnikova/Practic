def get_multiplied_digits(number):
    str_number = str(number)
    if len((str_number[1:])) > 0:
        first = int(str_number[0])
        return first * get_multiplied_digits(int(str_number[1:]))
    else:
        return number


result = get_multiplied_digits(40203)
result1 = get_multiplied_digits(425)
result2 = get_multiplied_digits(3020506)
print(result)
print(result1)
print(result2)
