"""EvgeniyK: спасибо большое!
LinaTroshka: лайк и подписка!
Sergey Karandeev: крутое видео!
Евгений Соснин: обожаю
EvgeniyK: это повтор?
Sergey Karandeev: нет, это новое видео"""

#import sys

#lst_in = list(map(str.strip, sys.stdin.readlines()))

lst_in = ['EvgeniyK: спасибо большое!', 'LinaTroshka: лайк и подписка!', 'Sergey Karandeev: крутое видео!', 'Евгений Соснин: обожаю', 'EvgeniyK: это повтор?', 'Sergey Karandeev: нет, это новое видео']

a = [i.split(': ') for i in lst_in]
b = (dict(a)).keys()
c = set(b)
print(len(c))