"""Написать функцию по решению квадратных
уравнений."""


def kvadrat_x1_x2(a, b, c: int) -> [float, float, str]:
    d = b ** 2 - 4 * a * c
    if d > 0:
        x_1 = (- (b / 2) - d ** 0.5) / a
        x_2 = (- (b / 2) + d ** 0.5) / a
        print(f'x_1 = {x_1}, x_2 = {x_2}')
        return x_1, x_2
    elif d == 0:
        x_1 = (- (b / 2)) / a
        print(f'x_1 = {x_1}')
        return x_1
    else:
        print(f'Нет корней')


kvadrat_x1_x2(1, 0, 0)
