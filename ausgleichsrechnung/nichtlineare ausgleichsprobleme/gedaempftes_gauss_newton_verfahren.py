# -*- coding: utf-8 -*-

import sympy as sp
import scipy.optimize as op
import numpy as np
import matplotlib.pyplot as plt


def gauss_newton(g, Dg, lam0, tol=1e-5, max_iter=30, pmax=5, damping=True, print_info=False):
    """
    Implementation des Gauss-Newton-Verfahrens für nichtlineare Ausgleichsprobleme.
    Gegeben ist eine Funktion g, die Jacobi-Matrix von g sowie ein Startvektor 𝞴_0.
    Die Funktion g kann dabei hergeleitet werden aus der zu fittenden Funktion minus die Stützstellen.
    Bspw.: `sp.Matrix([y[k] - f(x[k], l) for k in range(len(x))])` wobei y die Y-Werte der Stützstellen sind,
    f(x, l) die zu fittende Funktion mit der Liste von 𝞴_n Variablen und x die X-Werte der Stützstellen.

    :param Dg: Die Jacobi-Matrix für g
    :param pmax: Die Maximale Dämpfung. Dabei ist 2 = halbieren, 3 = 2^3, etc.
    :return: Der 𝞴-Vektor sowie die Anzahl benötigter Iterationen.
    """
    k = 0
    lam = np.copy(lam0)
    increment = tol + 1
    err_func = np.linalg.norm(g(lam)) ** 2

    while increment >= tol and k <= max_iter:
        # QR-Zerlegung von Dg(lam)
        Q, R = np.linalg.qr(Dg(lam))
        delta = np.linalg.solve(R, -Q.T @ g(lam)).flatten()
        p = 0

        # Errechnen des damping-Faktors
        while damping and p <= pmax and np.linalg.norm(g(lam + (delta / 2 ** p)), 2) ** 2 >= err_func:
            p = p + 1
        if p == pmax + 1:
            p = 0

        # Update des Vektors Lambda
        lam = lam + delta / 2 ** p
        err_func = np.linalg.norm(g(lam)) ** 2
        increment = np.linalg.norm(delta / 2 ** p)
        k = k + 1

        if print_info:
            print(f'Dämpfungsexponent: {p}')
            print('Iteration: ', k)
            print('lambda = ', lam)
            print('Inkrement = ', increment)
            print('Fehlerfunktional =', err_func)
    return lam, k


def err_func(x):
    return np.linalg.norm(g(x), 2) ** 2


# ----------------------------------------------------------------------------------------------------------------------
# Beispielrechnung:
# ----------------------------------------------------------------------------------------------------------------------

# noinspection PyShadowingNames
def f(x, l):
    factor = 10 ** (l[2] + l[3] * x)
    return (l[0] + l[1] * factor) / (1 + factor)


if __name__ == '__main__':
    x = np.array([2., 2.5, 3., 3.5, 4., 4.5, 5., 5.5, 6., 6.5, 7., 7.5, 8., 8.5, 9., 9.5])

    y = np.array([159.57209984, 159.8851819, 159.89378952, 160.30305273,
                  160.84630757, 160.94703969, 161.56961845, 162.31468058,
                  162.32140561, 162.88880047, 163.53234609, 163.85817086,
                  163.55339958, 163.86393263, 163.90535931, 163.44385491])
    sp.init_printing(pretty_print=True)

    lam0 = np.array([100, 120, 3, -1], dtype=np.float64)        # Initialisierung des Start-Lambda Vektors
    l = sp.symbols('l0 l1 l2 l3')                               # Erstellen der Variablen
    g = sp.Matrix([y[k] - f(x[k], l) for k in range(len(x))])   # Definition der Funktion g(x), welche eine
                                                                # den absoluten Fehler der gefitteten Funktion zu
                                                                # den Stützstellen ist.
    Dg = g.jacobian(l)                                          # Bilden der Jacobi-Matrix der normalisierten Funktion

    g = sp.lambdify([l], g, 'numpy')
    Dg = sp.lambdify([l], Dg, 'numpy')

    lam, _k = gauss_newton(g, Dg, lam0, tol=1e-5, max_iter=30, pmax=5, damping=True)

    '''
    Das ungedämpfte Newton-Verfahren konvergiert für dieses Beispiel
    nicht mehr, da nach der 12 Iteration das Fehlerfunktional zu gross wird
    '''

    # Kontrolle zu der Fehlerminimierungsfunktion von Scipy
    xopt = op.fmin(err_func, lam0)
    print(f'scipy Minimum: {xopt}')

    # Visualisierung
    x_scale = np.arange(1, 10, .5)
    plt.plot(x_scale, f(x_scale, xopt), color='blue')
    plt.plot(x_scale, f(x_scale, lam), color='red')
    plt.plot(x, y, 'o', color='gray')
    plt.grid(True)
    plt.show()
