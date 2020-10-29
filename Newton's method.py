def naive_Newton(f, dfdx, x, eps):
  x1 = x+eps*2
  while abs(x1-x) > eps:
    x1 = x
    x = x - float(f(x))/dfdx(x)
  return x

def f(x):
  return x**2 - 9
def dfdx(x):
  return 2*x

print(naive_Newton(f, dfdx, 1, 0.001))