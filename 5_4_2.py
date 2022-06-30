"""Вводится строка с номером телефона. Ожидается формат ввода:
+7(xxx)xxx-xx-xx
где x - это цифра. Размер введенных символов считается верным (то есть,
не может быть, чтобы отсутствовала какая-либо цифра или была лишняя).
Необходимо проверить, что введенная строка соответствует этому формату.
Вывести ДА, если соответствует и НЕТ - в противном случае.
Sample Input:
+7(123)456-78-99
Sample Output:
ДА
"""
#a = '+7(123)456-78-99'
a = input()
for z, v in enumerate(a):
    if z == 0 and v == '+':
        continue
    if z == 1 and v == '7':
        continue
    if z == 2 and v == '(':
        continue
    if z == 6 and v == ')':
        continue
    if z == 10 and v == '-':
        continue
    if z == 13 and v == '-':
        continue
    if z in range(3, len(a) - 1) and v.isdigit() == True:
        continue
    if v == a[len(a) - 1] and v.isdigit() == True:
        print('ДА')
        break
    else:
        print('НЕТ')
        break
