import math


class Figure:
    sides_count = 0

    def __init__(self,  color=(0, 0, 0), *sides):
        self.__color = color
        self.__sides = sides
        self.filled = False
        self.set_color(*color)
        self.set_sides(*sides)

    def get_color(self):
        return self.__color

    @staticmethod
    def __is_valid_color(r, g, b):
        return 0 <= r <= 255 and 0 <= g <= 255 and 0 <= b <= 255

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]
        return self.__color

    def __is_valid_sides(self, *args):
        return all(isinstance(s, int) and s > 0 for s in args) and len(args) == self.sides_count

    def get_sides(self):
        return self.__sides

    def __len__(self):
        return sum(self.__sides)

    def set_sides(self, *new_sides):
        if self.__is_valid_sides(*new_sides):
            self.__sides = list(new_sides)
        elif len(new_sides) == 1:
            self.__sides = [int(new_sides[0]) for _ in range(self.sides_count)]

        return self.__sides


class Circle(Figure):
    sides_count = 1

    def __init__(self, color=(0, 0, 0), *sides):
        super().__init__(color, *sides)
        self.__sides = [1] if len(sides) != self.sides_count else list(sides)
        self.__radius = self.__sides[0] / (2 * math.pi)

    def get_square(self):
        return 3.14 * self.__radius**2


class Triangle(Figure):
    sides_count = 3

    def __init__(self, color=(0, 0, 0), *sides):
        super().__init__(color, *sides)
        self.__sides = [1] * self.sides_count if len(sides) != self.sides_count else sides

    def get_square(self, *sides):
        p = len(self) / 2
        square = math.sqrt(p * (p - sides[0]) * (p - sides[1]) * (p - sides[2]))
        return square


class Cube(Figure):
    sides_count = 12

    def __init__(self, color=(0, 0, 0), *sides):
        super().__init__(color, *sides)
        self.__sides = [1] * self.sides_count if len(set(sides)) != 1 \
            else [int(sides[0]) for _ in range(self.sides_count)]

    def get_volume(self):
        return self.__sides[0] ** 3


circle1 = Circle((200, 200, 100), 10)  # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)
#
# # Проверка на изменение цветов:
circle1.set_color(55, 66, 77)  # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15)  # Не изменится
print(cube1.get_color())
# #
# #
# # # Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5)  # Не изменится
print(cube1.get_sides())
circle1.set_sides(15)  # Изменится
print(circle1.get_sides())
# #
# # Проверка периметра (круга), это и есть длина:
print(len(circle1))
# #
# # # Проверка объёма (куба):
print(cube1.get_volume())


"""
[55, 66, 77]
[222, 35, 130]
[6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6]
[15]
15
216
"""
