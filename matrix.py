"""Дана целочисленная матрица А[n,m]. Посчитать
количество элементов матрицы, превосходящих среднее
арифметическое значение элементов матрицы и сумма
индексов которых четна."""

import numpy as np
import random
n, m = 3, 4
kol = 0
A = [[random.randrange(0, 9) for i in range(n)] for j in range(m)]
print(A)
b = np.array(A)
print(b, type(b))
sum_b = sum(sum(b))
print(sum_b)
for k in range(m):
    for l in range(n):
        if b[k][l] > (sum_b / (n * m)) and (k + l) % 2 == 0:
            print(f'{k} + {l} = {b[k][l]}')
            kol += b[k][l]
print(kol)
