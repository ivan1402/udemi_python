"""
Вводятся данные в формате ключ=значение в одну строчку через пробел. Необходимо на их основе создать словарь, затем проверить,
существуют ли в нем ключи со значениями: 'house', 'True' и '5' (все ключи - строки). Если все они существуют, то вывести на экран ДА,
иначе - НЕТ.
Sample Input:
вологда=город house=дом True=1 5=отлично 9=божественно
Sample Output:
ДА
"""
q = ['house', 'True', '5']
lst = [i.split(sep='=') for i in input().split(sep=' ')]
d = dict(lst)
j = 0
s = 'НЕТ'
#print(len(q))
while j != len(q):
    if q[j] in d.keys():
        s = 'ДА'
        #print(d.keys(), s, j)
        j += 1
    else:
        s = 'НЕТ'
        #print(d.keys(), s, j)
        j += 1
        break
print(s)

