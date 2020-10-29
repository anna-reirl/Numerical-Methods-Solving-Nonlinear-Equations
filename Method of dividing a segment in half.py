# Defining Function
def f(x):
    return x ** 3 - 5 * x - 9


# Implementing Bisection Method
def bisection(x0, x1, e):
    step = 1
    print('\n\n*** Метод деление отрезка пополам ***')
    condition = True
    while condition:
        x2 = (x0 + x1) / 2
        print('Iteration-%d, x2 = %0.6f and f(x2) = %0.6f' % (step, x2, f(x2)))

        if f(x0) * f(x2) < 0:
            x1 = x2
        else:
            x0 = x2

        step = step + 1
        condition = abs(f(x2)) > e

    print('\nRequired Root is : %0.8f' % x2)


# Input Section
x0 = input('Первое предположение: ')
x1 = input('Второе предположение: ')
e = input('Допустимая ошибка: ')

# Converting input to float
x0 = float(x0)
x1 = float(x1)
e = float(e)

# Checking Correctness of initial guess values and bisecting
if f(x0) * f(x1) > 0.0:
    print('Приведенные предполагаемые значения не заключают в скобки корень.')
    print('Попробуйте еще раз с другими значениями предположений.')
else:
    bisection(x0, x1, e)