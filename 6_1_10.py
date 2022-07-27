"""
ustanovka-i-zapusk-yazyka
ustanovka-i-poryadok-raboty-pycharm
peremennyye-operator-prisvaivaniya-tipy-dannykh
arifmeticheskiye-operatsii
ustanovka-i-poryadok-raboty-pycharm
"""
import sys
lst_in = list(map(str.strip, sys.stdin.readlines()))
# lst_in = ['ustanovka-i-zapusk-yazyka', 'ustanovka-i-poryadok-raboty-pycharm', 'peremennyye-operator-prisvaivaniya-tipy-dannykh', 'arifmeticheskiye-operatsii', 'ustanovka-i-poryadok-raboty-pycharm']
d = {}
i = 0
while i != len(lst_in):
    if lst_in[i] not in d.keys():
        d[lst_in[i]] = ('HTML-страница для адреса ' + lst_in[i])
        print(d[lst_in[i]])
        i += 1
    elif lst_in[i] in d.keys():
        print(f'Взято из кэша: {d[lst_in[i]]}')
        i += 1
