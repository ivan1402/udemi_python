"""
3 Сергей
5 Николай
4 Елена
7 Владимир
5 Юлия
4 Светлана
"""
#import sys
#lst_in = list(map(str.strip, sys.stdin.readlines()))
lst_in = ['3 Сергей', '5 Николай', '4 Елена', '7 Владимир', '5 Юлия', '4 Светлана']
lst_off = [i.split(' ') for i in lst_in]
print(lst_off)
d = {}
d = {i[0]: [j[1] for j in lst_off if j[0] == i[0]] for i in lst_off if i[0] not in d}
z = [j[1] for j in lst_off]
print(z)
print(d)
for x, y in d.items():
    print(x, ", ".join(y))


