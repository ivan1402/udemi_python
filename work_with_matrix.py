"""Написать программу для работы с матрицами:
Создание
Вывод
Сумма всех элементов
Нахождение максимального элемента
Нахождение минимального элемента."""
import numpy as np


def create_matrix(n, m, a, b):
    import random
    matrix = [[random.randint(a, b) for i in range(n)] for j in range(m)]
    print(matrix)
    return matrix
#create_matrix(3, 3, 0, 10)

def sum_el_matrix(A):
    summ = sum(sum(np.array(A)))
    print(summ)
    return summ
sum_el_matrix(create_matrix(3, 3, 0, 10))

def max_element_matrix(A):
    print(max(map(max, A)))
    return max(map(max, A))
max_element_matrix(create_matrix(3, 3, 0, 100))

def min_element_matrix(A):
    print(min(map(min, A)))
    return min(map(min, A))
min_element_matrix(create_matrix(3, 3, 0, 100))