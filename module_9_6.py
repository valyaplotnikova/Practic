def all_variants(text):
    for k in range(len(text)):
        for j in range(len(text)-k):
            yield text[j:j+1+k]


a = all_variants("abc")
for i in a:
    print(i)


"""
Вывод на консоль:
a
b
c
ab
bc
abc
"""