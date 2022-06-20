"""def print_list(*args):
    print(args)
print_list(1,2,3,4)"""

"""Создать функцию, принимающая на вход неопределенное
количество аргументом и возвращающая сумму args[i] * i
Пример: args = [4,3,2,1], 4 * 0 + 3 * 1 + 2 * 2 + 1 * 3 = 10"""

"""def summ_ar(*args):
    summ_ = 0
    k = 0
    for i in args:
        summ_ += k * i
        k += 1
        print(summ_)
    return summ_
summ_ar(1, 2, 3, 4, 5555)"""

"""Создать функцию, которая принимает на вход
неопределенное количество именных
аргументов и выводит на экран те из них,
длина ключа которых четна."""

"""#Сбор аргументов в словарь

def my_func(**kwargs):
    for key, value in kwargs.items():
        if len(str(value)) % 2 == 0:
            print(key, value, len(str(value)))
my_func(a = 5, b ='sds4', c = 1234, d = 0, e = 123456)"""


"""Написать функцию принимающая на вход
неопределенным количеством аргументов и именованный
аргумент mean_type. В зависимости от mean_type вернуть
среднеарифметическое либо среднегеометрическое.
Написать программу в виде трех функций."""

"""def fun_(*args, mean_type = 1):
    if mean_type:
        return sred_arif(*args)
    else:
        return sred_geom(*args)

def sred_arif(*args):
    s = sum(args) / len(args)
    print(s)
    return s

def sred_geom(*args):
    proizved = 1
    for i in args:
        proizved *= i
        sred_geometr = proizved ** (1 / len(args))
        print(sred_geometr)
        return sred_geometr

fun_(1, 2, 3, 4, 5)"""