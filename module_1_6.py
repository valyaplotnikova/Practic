my_dict = {"Valya": 1986, "Sava": 2019, "Matvey": 1986}
print(f"Dict: {my_dict}")
print(f"Existing value: {my_dict['Valya']}")
print(f"Not existing value: {my_dict.get("Oleg")}")
my_dict.update({"Galya": 1953, "Lesha": 1978})
del_ = my_dict.pop("Lesha")
print(f"Deleted value: {del_}")
print(f"Modified dictionary: {my_dict}")

my_set = {1, 1, 2, 2, 3, 3, 3}
print(f"Set: {my_set}")
my_set.add(10)
my_set.add(15)
my_set.discard(2)
print(f"Modified set: {my_set}")
