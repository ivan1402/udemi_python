"""В виде строки записано арифметическое выражение, например:
"10 + 25 - 12" или "10 + 25 - 12 + 20 - 1 + 3" и т. д.
То есть, количество действий может быть разным.
Необходимо выполнить вычисление и результат отобразить на экране.
Полагается, что в качестве арифметических операций здесь используется только сложение
(+) и вычитание (-), а в качестве операндов - целые неотрицательные числа. Следует учесть,
что эти операторы могут быть записаны как с пробелами, так и без них.
Sample Input:
10+25 - 12
Sample Output:
23
"""
# удаляем пробелы
#

#a = '10+25 - 12'
#print(f'a = {a}')
a = input()
b = (a.replace(' ', ''))
l = list(b)
l_minus = []
l_plus =[]
i = len(l) - 1
while i >= 0:
    if l[i - 1] != '-' and l[i - 1] != '+' and i != 0:
        l[i - 1] = l[i - 1] + l[i]
        l.pop(i)
        #print(f'i = {i}         l = {l}')
        i -= 1
    elif l[i - 1] == '-':
        l_minus.append(int(l[i]))
        l.pop(i)
        l.pop(i - 1)
        #print(f'i = {i}         l = {l}      l.minus = {l_minus}')
        i -= 2
    elif l[i - 1] == '+':
        l_plus.append(int(l[i]))
        l.pop(i)
        l.pop(i - 1)
        #print(f'i = {i}         l = {l}      l_plus = {l_plus}')
        i -= 2
    elif i == 0:
        l_plus.append(int(l[i]))
        l.pop(i)
        #print(f'i = {i}         l = {l}      l_plus = {l_plus}')
        i -= 1
#print(f'l_plus = {l_plus}')
#print(f'l_minus = {l_minus}')
sum_l_plus = sum(l_plus)
sum_l_minus = sum(l_minus)
#print(sum_l_plus, sum_l_minus)
summ = sum_l_plus - sum_l_minus
print(summ)
