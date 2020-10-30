# # Defining Function
# def f(x):
#     return x ** 3 - 5 * x - 9
#
#
# # Implementing Bisection Method
# def bisection(x0, x1, e):
#     step = 1
#     print('\n\n*** Метод деление отрезка пополам ***')
#     condition = True
#     while condition:
#         x2 = (x0 + x1) / 2
#         print('Iteration-%d, x2 = %0.6f and f(x2) = %0.6f' % (step, x2, f(x2)))
#
#         if f(x0) * f(x2) < 0:
#             x1 = x2
#         else:
#             x0 = x2
#
#         step = step + 1
#         condition = abs(f(x2)) > e
#
#     print('\nRequired Root is : %0.8f' % x2)
#
#
# # Input Section
# x0 = input('Первое предположение: ')
# x1 = input('Второе предположение: ')
# e = input('Допустимая ошибка: ')
#
# # Converting input to float
# x0 = float(x0)
# x1 = float(x1)
# e = float(e)
#
# # Checking Correctness of initial guess values and bisecting
# if f(x0) * f(x1) > 0.0:
#     print('Приведенные предполагаемые значения не заключают в скобки корень.')
#     print('Попробуйте еще раз с другими значениями предположений.')
# else:
#     bisection(x0, x1, e)
# _______________________________________


# Bisection Method.
# The function is x^3 - x^2  + 2
def func(x):
    return x * x * x - x * x + 2


# Prints root of func(x)
# with error of EPSILON
def bisection(a, b):
    if (func(a) * func(b) >= 0):
        print("You have not assumed right a and b\n")
        return

    c = a
    while ((b - a) >= 0.01):

        # Нахожу среднюю точку
        c = (a + b) / 2

        # Проверяю является ли средняя точка корнем
        if (func(c) == 0.0):
            break

        # Decide the side to repeat the steps
        if (func(c) * func(a) < 0):
            b = c
        else:
            a = c

    print("Значения корня равно:", "%.4f" % c)


# Ориентировочные начальные значения
a = -200
b = 300
bisection(a, b)
