import numpy as np
import sympy as sp

a, b = sp.symbols('a b')
x = np.array([0, 1, 2, 3, 4])
y = np.array([3, 1, 0.5, 0.2, 0.05])
f1 = 0
for i in range(0, 5):
    f1 = f1 + (y[i] - a * sp.exp(b * x[i])) * sp.exp(b * x[i])
f1 = -2 * f1

f2 = 0
for i in range(0, 5):
    f2 = f2 + (y[i] - a * sp.exp(b * x[i])) * a * sp.exp(b * x[i]) * x[i]
f2 = -2 * f2

f = sp.Matrix([f1, f2])
lam = sp.Matrix([a, b])  # Achtung: die Unbekannten sind a und b (nicht x)
Df = f.jacobian(lam)
f = sp.lambdify([[[a], [b]]], f, "numpy")
Df = sp.lambdify([[[a], [b]]], Df, "numpy")


# Newtons Methode für Systeme
def newton(f, Df, x0, tol):
    n = 0
    x = np.copy(x0)
    err = np.linalg.norm(f(x), 2)
    while err > tol:
        delta = np.linalg.solve(Df(x), - f(x))
        x = x + delta
        err = np.linalg.norm(f(x), 2)
        n = n + 1
    return x, n


if __name__ == '__main__':
    tol = 1
    e = 5
    x0 = np.array([[3, -1]]).T
    [xn, n] = newton(f, Df, x0, tol)
    print('x_' + str(n) + ' = ' + str(np.reshape(xn, 2)))
