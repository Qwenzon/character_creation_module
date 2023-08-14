from math import sqrt


def calculatesquareroot(number):
    """Вычисляет квадратный корень."""
    return sqrt(number)


def calc(your_number):
    """Check your number."""
    if (your_number <= 0):
        return
    a = calculatesquareroot(your_number)
    print(f'Мы вычислили квадратный корень из введённого вами числа.'
          f' Это будет: {a}')
    return


message = ('Добро пожаловать в самую лучшую программу'
           ' для вычисления квадратного корня из заданного числа')
print(message)
calc(25.5)
