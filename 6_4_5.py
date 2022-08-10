a = 'Python 3.9.11 - best language!'
# a = input()
b = [i for i in a if i.isdigit() == True]
c = set(b)
if b == []:
    print('НЕТ')
else:
    print(*sorted(c))
