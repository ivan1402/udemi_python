"""Написать программу для нахождения
факториала. Факториал натурального числа n
определяется как произведение всех
натуральных чисел от 1 до n включительно"""

def faktorial(n):
    faktorial = 1
    while n > 1:
        faktorial *= n
        n -= 1
    print(faktorial)
    return faktorial
faktorial(5)
