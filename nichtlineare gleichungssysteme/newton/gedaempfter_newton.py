import sympy as sp
import numpy as np


def damped_newton(f, Df, x0, tol, damping=2):
    """
    Löst das Gleichungssystem mithilfe dem gedämpften Newton-Verfahren für Systeme.

    :param f: Das Gleichungssystem. F ist eine 1-dimensionale Matrix mit aus Funktionen
    :param Df: Die Jacobi-Matrix von f
    :param x0: Der Start-Vektor. Dieser muss die gleichen Dimensionen wie f haben.
    :param damping: Die Dämpfung, welche standardmäßig 2 ist, was den Schritt halbiert.
    :return Ein Vektor x der selben Dimension wie f mit der möglichen Lösung
    """
    x = np.copy(x0)
    for i in range(1, 100):
        fx = f(x)
        d = delta(fx, Df, x) / damping
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
    x1, x2, x3 = sp.symbols('x1 x2 x3')
    f = sp.Matrix([
        x1 + x2 ** 2 - x3 ** 2 - 13,
        sp.ln(x2 / 4) + sp.exp(0.5 * x3 - 1) - 1,
        (x2 - 3) ** 2 - x3 ** 3 + 7
    ])

    Df = sp.lambdify([(x1, x2, x3)], f.jacobian(sp.Matrix([x1, x2, x3])), 'numpy')
    f = sp.lambdify([(x1, x2, x3)], f, 'numpy')

    print(damped_newton(f, Df, np.array([1.5, 3, 2.5]), 1e-5))
