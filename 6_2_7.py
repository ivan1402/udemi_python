#N = int(input())
#N = 10
K = N * 1000
things = {'карандаш': 20, 'зеркальце': 100, 'зонт': 500, 'рубашка': 300,
          'брюки': 1000, 'бумага': 200, 'молоток': 600, 'пила': 400, 'удочка': 1200,
          'расческа': 40, 'котелок': 820, 'палатка': 5240, 'брезент': 2130, 'спички': 10}
things_in = {y: x for x, y in things.items()}
#print(things_in)
things_sort = sorted(things.values())
#print(things_sort[::-1])
list_off = []
for i in (things_sort[::-1]):
    if K - i >= 0:
        list_off.append(i)
        K -= i
print(*[things_in.get(i) for i in list_off])


