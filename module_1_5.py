immutable_var = (1, 5, False, 'name', [1, 2, 3])
print(f"Immutable tuple: {immutable_var}")
# immutable_var[0] = 2
"""
Кортеж является неизменяемым типом данных
"""
mutable_list = [1, 5, False, 'name', [1, 2, 3]]
mutable_list[2] = True
mutable_list[0] = 15
mutable_list[3] = "last_name"
print(f"Mutable list: {mutable_list}")
