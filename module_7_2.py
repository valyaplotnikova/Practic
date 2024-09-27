def custom_write(file_name: str, strings: list[str]) -> dict:
    """
    Записывает в файл file_name все строки из списка strings, каждая на новой строке.
    Возвращает словарь strings_positions, где ключом будет кортеж (<номер строки>, <байт начала строки>),
    а значением - записываемая строка
    :param file_name: str
    :param strings: list[str]
    :return: dict
    """
    count = 0
    strings_positions = {}
    if not file_name:
        file = open(file_name, 'x', encoding="UTF-8")
        file.close()
    file = open(file_name, 'a', encoding="UTF-8")
    for st in strings:
        count += 1
        st_number = count
        st_byte = file.tell()
        file.write(st)
        file.write('\n')
        strings_positions[(st_number, st_byte,)] = st

    file.close()

    return strings_positions


info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
    print(elem)


"""
((1, 0), 'Text for tell.')
((2, 16), 'Используйте кодировку utf-8.')
((3, 66), 'Because there are 2 languages!')
((4, 98), 'Спасибо!')
"""
