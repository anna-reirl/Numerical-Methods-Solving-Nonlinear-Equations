# def simpson(a, b, n, f):
#   sum = 0
#   inc = (b - a) / n
#   for k in range(n + 1):
#     x = a + (k * inc)
#     summand = f(x)
#     if (k != 0) and (k != n):
#       summand *= (2 + (2 * (k % 2)))
#     sum += summand
#   return ((b - a) / (3 * n)) * sum
#
# # Examples of use
# print(simpson(1, 2, 10, lambda x: 1 / x))
# print(simpson(1, 4, 6, lambda x: 1 / x))
#
# import math
# print(simpson(0, 1, 6, lambda x: 1 / math.sqrt(1 + x * x)))

# Эта программа реализует правило Симпсона 1/3 для нахождения приближенного значения численного интегрирования.
# В этой программе на Python, lower_limit и upper_limit - это нижний и верхний предел интеграции,
# sub_interval - это номер подинтервала, используемый при нахождении суммы, а функция f (x), которая будет интегрирована методом Симпсона 1/3,
# определяется с использованием определения функции Python def f():

# Simpson's 1/3 Rule

# Определяю функцию для интегрирования
def f(x):
    return 1 / (1 + x ** 2)


# Implementing Simpson's 1/3
def simpson13(x0, xn, n):
    # расчет размера шага
    h = (xn - x0) / n

    # Нахождение суммы
    integration = f(x0) + f(xn)

    for i in range(1, n):
        k = x0 + i * h

        if i % 2 == 0:
            integration = integration + 2 * f(k)
        else:
            integration = integration + 4 * f(k)

    # Нахождение окончательного значения интеграла
    integration = integration * h / 3

    return integration


# Input section
lower_limit = float(input("Введите нижний предел интегрирования: "))
upper_limit = float(input("Введите верхний предел интегрирования: "))
sub_interval = int(input("Введите количество подинтервалов: "))

# Call trapezoidal() method and get result
result = simpson13(lower_limit, upper_limit, sub_interval)
print("Результат интегрирования по методу Симпсона 1/3: %0.6f" % (result))