# function takes value of x
# and returns f(x)
def f(x):
    # as x^3+x-1
    f = pow(x, 3) + x - 1
    return f


def secant(x1, x2, E):
    n = 0
    xm = 0
    x0 = 0
    c = 0
    if (f(x1) * f(x2) < 0):
        while True:

            # рассчитать промежуточное значение
            x0 = ((x1 * f(x2) - x2 * f(x1)) /
                  (f(x2) - f(x1)))

            # проверяем, является ли x0 корнем
            # уравнение или нет
            c = f(x1) * f(x0)

            # обновить значение интервала
            x1 = x2
            x2 = x0

            # обновить номер итерации
            n += 1

            # если x0 - корень уравнения
            # затем прервать цикл
            if (c == 0):
                break
            xm = ((x1 * f(x2) - x2 * f(x1)) /
                  (f(x2) - f(x1)))

            if (abs(xm - x0) < E):
                break

        print("Корень данного уравнения = ",
              round(x0, 6))
        print("Кол-во итераций = ", n)

    else:
        print("Не удается найти корень в заданном интервале")


# initializing the values
x1 = 0
x2 = 1
E = 0.0001
secant(x1, x2, E)

