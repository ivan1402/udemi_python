"""#Дан список слов. Сгенерировать новый список с
#перевернутыми словами

list_1 = ['Ivan', 'Gleb', 'ABc', 'Popi']
list_2 = [i[::-1] for i in list_1]
print(list_2)
#['navI', 'belG', 'cBA', 'ipoP']"""

"""#Дан список словарей. Каждый словарь
#описывает машину(серийный номер и год
#выпуска). Создать новый список со всеми
#машинами, год выпуска которых больше n

cars = [
    {'name': 'mers', 'number': 7800, 'year': 2000},
    {'name': 'ford', 'number': 1230, 'year': 2008},
    {'name': 'bmv', 'number': 5500, 'year': 2007}
]
n = 2002

cars_n = [dict_cars for dict_cars in cars if dict_cars['year'] > n]
print(cars_n)
#[{'name': 'ford', 'number': 1230, 'year': 2008}, {'name': 'bmv', 'number': 5500, 'year': 2007}]
"""

"""old_dict = {'aa': 1, 'b': 2, 'cccc': 3}
new_dict = {value: key for key, value in old_dict.items()}
print(new_dict)"""

"""Дан список чисел. Посчитать сколько раз
встречается каждое число. Использовать функцию.
Подсказка: для хранения данных использовать словарь. Для проверки
нахождения элемента в словаре использовать метод get(), либо оператор in"""
"""
list_numb = [1, 2, 3, 4, 5, 2, 1, 2, 3]


def skolko_povtorov(list_a: list) -> dict:
    dict_povtorov = {}
    for elem in list_a:
        if dict_povtorov.get(elem, None):
            dict_povtorov[elem] += 1
        else:
            dict_povtorov[elem] = 1
    print(dict_povtorov)
    return dict_povtorov


skolko_povtorov(list_numb)
"""

"""Рассчитать значение х определив и использовав необходимую функции."""


"""def fun_x(a, b, c: int) -> int:
    x = (a ** 0.5 + a + b ** 0.5 + b + c ** 0.5 + c) / 2
    print(x)
    return x


fun_x(5, 12, 19)"""

"""Описать функцию is_power_n( k , n ) логического типа, возвращающую
True, если целый параметр k (> 0) является степенью числа n (> 1), и False
в противном случае. Дано число n (> 1) и набор из 10 целых положитель-
ных чисел. С помощью функции is_power_n найти количество степеней чис-
ла N в данном наборе."""

"""
def is_power_n(k, n: int) -> [float, bool]:
    summ_step = 0
    list_numb = [5, 7, 4, 3, 18, 21, 33, 2, 9, 2, 2] #11
    if k > 0:
        for i in list_numb:
            for x in range(1, 10):
                if n ** x == i:
                    summ_step += x
        print(summ_step)
        return summ_step
    else:
        print(False)


is_power_n(1, 2)"""

"""Дан массив целых чисел A. Найти суммы
положительных и отрицательных элементов
массива, используя функцию определения
суммы."""


def funk_summa_(a: list) -> [int, int]:
    sum_poloj = 0
    sum_otr = 0
    k = len(a)
    while k > 0:
        for i in range(len(a)):
            if a[i] > 0:
                sum_poloj += a[i]
            else:
                sum_otr += a[i]
        print(f'sum_poloj = {sum_poloj}\n'
              f'sum_otr = {sum_otr}')
        return sum_poloj, sum_otr


a = [-1, 2, 3, 4, 5, -3, 5, -5, 10, 33, -3]
funk_summa_(a)
