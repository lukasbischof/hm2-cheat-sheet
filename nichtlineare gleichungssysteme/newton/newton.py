import sympy as sp
from matplotlib import style
import numpy as np

style.use('ggplot')

'''
Verwendung der Funktion:
1. Initialisieren aller Funktionen und Variablen
2. Jacobi-Matrix bilden mithilfe von jacobian(X). 
   X ist dabei der Vektor aller verwendeten Variablen. (bspw. x1, x2, ...)
3. Startwert festlegen
3. Methode mit lambda-Funktionen aufrufen. 
'''


# noinspection PyShadowingNames
def newton(f, Df, x0, tol):
    """
    Löst das Gleichungssystem mithilfe dem Newton-Verfahren für Systeme.

    :param f: Das Gleichungssystem. F ist eine 1-dimensionale Matrix mit aus Funktionen
    :param Df: Die Jacobi-Matrix von f
    :param x0: Der Start-Vektor. Dieser muss die gleichen Dimensionen wie f haben.
    """
    x = np.copy(x0)
    for i in range(1, 100):
        fx = f(x)
        d = delta(fx, Df, x)
        x = x + d

        if np.linalg.norm(fx, 2) < tol:
            break
    return x


def delta(b, Df, x):
    return np.linalg.solve(Df(x), -b).transpose()[0]


# ----------------------------------------------------------------------------------------------------------------------
# Beispielrechnung:
# ----------------------------------------------------------------------------------------------------------------------

if __name__ == '__main__':
    x, y = sp.symbols('x y')
    f1 = x ** 2 / 186 ** 2 - y ** 2 / (300 ** 2 - 186 ** 2) - 1
    f2 = (y - 500) ** 2 / 279 ** 2 - (x - 300) ** 2 / (500 ** 2 - 279 ** 2) - 1
    f = sp.Matrix([f1, f2])
    Df = sp.lambdify([(x, y)], f.jacobian(sp.Matrix([x, y])), 'numpy')
    f = sp.lambdify([(x, y)], f, 'numpy')

    # Für den Plot des Systems kann folgender Code verwendet werden:
    # p1 = sp.plot_implicit(sp.Eq(f1, 0), (x, -2000, 2000), (y, -2000, 2000))
    # p2 = sp.plot_implicit(sp.Eq(f2, 0), (x, -2000, 2000), (y, -2000, 2000))
    # p1.append(p2[0])
    # p1.show()

    x0 = np.array([-230, 80])
    print(newton(f, Df, x0, 1e-5))
