"""Аргументы по умолчанию"""

"""Реализовать функцию возвращающую
матрицу. На вход принимает n - размерность
матрицы, random_from(по-умолчанию 1),
random_to(по-умолчанию(9))."""

"""def create_matrix(n, random_from = 1, random_to = 9):
    import random
    matrix = [[random.randrange(random_from, random_to) for i in range(n)] for j in range(n)]
    print(matrix)
    return matrix
create_matrix(3)"""

"""Именованные аргументы
def my_pow(number, power):
result = number ** power + 1
return result
result = my_pow(power=3, number=5)
print(result)"""