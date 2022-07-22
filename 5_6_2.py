"""Вводится список из URL-адресов (каждый с новой строки). Требуется в них заменить все пробелы на символ дефиса (-).
Следует учесть, что может быть несколько подряд идущих пробелов.
Результат преобразования вывести на экран в виде строк из URL-адресов.
P. S. Для считывания списка целиком в программе уже записаны начальные строчки.
Sample Input:
django chto  eto takoe    poryadok ustanovki
model mtv   marshrutizaciya funkcii  predstavleniya
marshrutizaciya  obrabotka isklyucheniy       zaprosov perenapravleniya
Sample Output:
django-chto-eto-takoe-poryadok-ustanovki
model-mtv-marshrutizaciya-funkcii-predstavleniya
marshrutizaciya-obrabotka-isklyucheniy-zaprosov-perenapravleniya
"""
import sys

# считывание списка из входного потока
# t = list(map(str.strip, sys.stdin.readlines()))
t = ['django chto  eto takoe    poryadok ustanovki', 'model mtv   marshrutizaciya funkcii  predstavleniya', 'marshrutizaciya  obrabotka isklyucheniy       zaprosov perenapravleniya']
for i, line in enumerate(t):

    while line.count('  '):
        line = line.replace('  ', ' ')
    while line.count(' '):
        line = line.replace(' ', '-')

    t[i] = line
    print(t[i])
print()