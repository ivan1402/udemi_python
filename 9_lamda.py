"""
lamda выражения
func = lambda x, y, z: x + y + z
"""

"""
Создать lambda функцию, которая
принимает на вход имя и выводит его
в формате “Hello, {name}”


def fun_name(x: str) -> None:
    print(f'Hello, {x}')


fun_name('Ivan')
"""

"""
Создать lambda функцию, которая
принимает на вход список имен и
выводит их в формате “Hello, {name}” в
другой список



def fun_name(x: list) -> list:
    list_2 = ['Hello, ' + i for i in list_x]
    print(list_2)
    return list_2


list_x = ['Ivan', 'Roma', 'Eva']
fun_name(list_x)
"""

"""
result = map(lambda x: x ** 2,
[1,2,3,4,5,6])
print(list(result))
"""

"""
Дан список чисел. Вернуть список, где каждый число переведено в строку


list_1 = [1, 2, 3, 4, 5, 6]
list_2 = map(lambda i: str(i), list_1)
print(list(list_2))
"""

"""
result = filter(lambda x: x % 2 == 0, [1, 2, 3, 4, 5, 6])
print(list(result))
"""

"""
Дан список имен, отфильтровать все имена, где есть буква k


list_x = ['Ivan', 'Roma', 'Eva', 'Ira']
list_2 = filter(lambda i: 'I' in i, list_x)
print(list(list_2))
"""

"""
#reduce()
from functools import reduce
result = reduce(lambda a, x: a + x ** 2, [1, 2, 3], 0)
print((result)) #>>> 14
"""

"""
Дан список чисел. Найти произведение всех чисел, которые кратны 3.

list_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12]
list_1 = filter(lambda i: i % 3 == 0, list_1)
from functools import reduce
result = reduce(lambda a, b: a * b, list_1, 1)
print(result)
"""



