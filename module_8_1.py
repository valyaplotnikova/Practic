def add_everything_up(a: int | float | str, b: int | float | str):
    """
    Принимает a и b, которые могут быть как числами(int, float), так и строками(str).
    Когда a и b окажутся разными типами (числом и строкой), то возвращает строковое представление этих
    двух данных вместе (в том же порядке). Во всех остальных случаях выполняет стандартные действия.
    """
    try:
        return a + b
    except TypeError:
        return str(a)+str(b)


print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))
