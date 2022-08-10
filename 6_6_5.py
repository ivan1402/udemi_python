# И что сказать и что сказать и нечего и точка
a = list(map(str, input().lower().split()))
print(a)
c = {i for i in a}
print(c)
b = {x: a.count(x) for x in c}
print(b.get('и', 0))
