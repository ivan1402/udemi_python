"""Вводится натуральное число n (то есть, целое положительное).
В цикле перебрать все целые числа в интервале [1; n] и сформировать
список из чисел, кратных 3 и 5 одновременно. Вывести полученную последовательность
чисел в виде строки через пробел, если значение n меньше 100. Иначе вывести на
экран сообщение "слишком большое значение n" (без кавычек).
Использовать в программе оператор else после цикла while.
Sample Input 1:
49
Sample Output 1:
15 30 45
Sample Input 2:
100
Sample Output 2:
слишком большое значение n
"""
n = int(input())
list_int = [i for i in range(1, n + 1)]
list_int_2 = []
k = 0
if n < 100:
    while k != n:
        if list_int[k] % 5 == 0 and list_int[k] % 3 == 0:
            list_int_2.append(list_int[k])
            k += 1
            continue
        else:
            k += 1
            continue
    print(*list_int_2)
else:
    print('слишком большое значение n')
