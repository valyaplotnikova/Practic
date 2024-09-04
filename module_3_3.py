def print_params(a=1, b='строка', c=True):
    print(a, b, c)


print_params(a=False, b=3.02, c="No")
print_params(a='15')
print_params()
print_params(b=25)
print_params(c=[1, 2, 3])

values_list = [1, 3.25, "mom"]
values_dict = {'a': '6', 'b': 6, 'c': 1.02}

print_params(*values_list)
print_params(**values_dict)

values_list_2 = ['1', 1]

print_params(*values_list_2, 42)
