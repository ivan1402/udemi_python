import sys
"""
5=отлично
4=хорошо
3=удовлетворительно

(3, 'удовлетворительно') (4, 'хорошо') (5, 'отлично')
"""
# lst_in = ['5=отлично', '4=хорошо', '3=удовлетворительно']

# lst_in = list(map(str.strip, sys.stdin.readlines()))
lst_in = list(map(str.strip, sys.stdin.readlines()))
# print(lst_in)
w = [[int(j) if j.isdigit()==True else j for j in i.split(sep='=')] for i in lst_in]
# print(w)
# print(w[0])
d = {}
i = 0
while i != len(w):
    d[w[i][0]] = w[i][1]
    i += 1
# print(d)
print(*sorted(d.items()))
