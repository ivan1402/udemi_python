"""Вводится натуральное число n. Необходимо найти все простые числа,
которые меньше этого числа n, то есть, в диапазоне [2; n).
Результат вывести на экран в строчку через пробел.
Sample Input:
11
Sample Output:
2 3 5 7
"""
"""n = list(range(2, int(input())))
s = n.copy()
i = len(n)
while i != 0:
    p = 0
    while p != len(n):
        if n[i-1] % n[p] == 0 and n[i-1] != n[p]:
            s.pop(i - 1)
            break
        p += 1
    i -= 1
print(*s) # 2 3 5 7
"""
n = int(input())
for i in range(2, n):
    for j in range(2, i):
        if i % j == 0:
            break
    else:
        print(i, end=' ') # 2 3 5 7