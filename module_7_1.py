class Product:

    name: str
    weight: float
    category: str

    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}'


class Shop:
    def __init__(self):
        self.__file_name = 'products.txt'
        self.data = []

    def get_products(self):
        if not self.__file_name:
            file = open(self.__file_name, 'x', encoding="UTF-8")
            file.close()
        file = open(self.__file_name, 'r', encoding="UTF-8")
        self.data = file.read()
        file.close()
        return self.data

    def add(self, *products):
        for product in products:
            if product.name in self.get_products():
                print(f'Продукт {product.name} уже есть в магазине')
            else:
                file = open(self.__file_name, 'a', encoding="UTF-8")
                file.write(product.__str__())
                file.write("\n")
                file.close()


s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2)  # __str__

s1.add(p1, p2, p3)

print(s1.get_products())

"""Вывод на консоль:
Первый запуск:
Spaghetti, 3.4, Groceries
Potato, 50.5, Vegetables
Spaghetti, 3.4, Groceries
Potato, 5.5, Vegetables
Второй запуск:
Spaghetti, 3.4, Groceries
Продукт Potato, 50.5, Vegetables уже есть в магазине
Продукт Spaghetti, 3.4, Groceries уже есть в магазине
Продукт Potato, 5.5, Vegetables уже есть в магазине
Potato, 50.5, Vegetables
Spaghetti, 3.4, Groceries
Potato, 5.5, Vegetables
"""
