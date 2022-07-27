# one=1 two=2 three=3
# ('one', 1) ('three', 3) ('two', 2)
# a, b, c = list(map(str, input().split()))
q = input().split()
print(q)
w = [[int(j) if j.isdigit()==True else j for j in i.split(sep='=')] for i in q]
print(w)
d = dict(w)
print(d)
print(*sorted(d.items()))
"""
one=1 two=2 three=3

['one=1', 'two=2', 'three=3']
[['one', 1], ['two', 2], ['three', 3]]
{'one': 1, 'two': 2, 'three': 3}
('one', 1) ('three', 3) ('two', 2)
"""
