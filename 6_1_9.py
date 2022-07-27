a = None
d = {}
while a != 0:
    a = int(input())
    if a == 0:
        break
    elif a in d.keys():
        print(f'значение из кэша: {d[a]}')
    else:
        b = round((a ** 0.5), 2)
        d[a] = b
        print(b)

