"""
Москва Тверь Уфа Казань Уфа Москва
Уфа Тверь Москва Казань
"""
a = input().split()
b = input().split()
#print(a, b, end='\n')
a = set(a)
b = set(b)
#print(a, b, end='\n')
if b <= a:
    print('ДА')
else:
    print('НЕТ')