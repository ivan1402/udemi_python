"""Вводится список городов в одну строчку через пробел. Необходимо создать итератор для
этого списка и с помощью итератора вывести на экран в столбик первые два значения (названия городов).
Sample Input:
Москва Лондон Берлин Пекин
Sample Output:
Москва
Лондон
"""
l = input().split()
it = iter(l)
print(next(it))
print(next(it))
