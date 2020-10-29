import math


def f(x):
    return x * x * x + x * x - 1


# Re-writing f(x)=0 to x = g(x)
def g(x):
    return 1 / math.sqrt(1 + x)


# Implementing Fixed Point Iteration Method
def fixedPointIteration(x0, e, N):
    print('\n\n*** Метод простых итераций***')
    step = 1
    flag = 1
    condition = True
    while condition:
        x1 = g(x0)
        print('Iteration-%d, x1 = %0.6f and f(x1) = %0.6f' % (step, x1, f(x1)))
        x0 = x1

        step = step + 1

        if step > N:
            flag = 0
            break

        condition = abs(f(x1)) > e

    if flag == 1:
        print('\nКорень: %0.8f' % x1)
    else:
        print('\nНе сходится.')


# Input Section
x0 = input('Введите первоначальное предположение: ')
e = input('Введите допустимую ошибку: ')
N = input('Введите максимальную итерацию: ')

# Converting x0 and e to float
x0 = float(x0)
e = float(e)

# Converting N to integer
N = int(N)

fixedPointIteration(x0, e, N)