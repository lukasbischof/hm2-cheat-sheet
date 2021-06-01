import numpy as np
import matplotlib.pyplot as plt

from differentialgleichungen.plot.quiver_plot import quiver_plot


def mittelpunkt_verfahren(f, a, b, n, y0):
    """
    :param f: Die Funktion f(x, y)
    :param a: Der Startwert x_0
    :param b: Der x-Wert, für welchen numerisch die Lösung berechnet werden soll
    :param n: Die Anzahl Schritte
    :param y0: Der Y-Startwert
    """
    y = np.zeros(n + 1)
    y[0] = y0
    h = (b - a) / n
    x = np.append(np.arange(a, b, h), b)

    for i in range(1, n + 1):
        x_half = x[i - 1] + h / 2
        y_half = y[i - 1] + (h / 2) * f(x[i - 1], y[i - 1])
        y[i] = y[i - 1] + h * f(x_half, y_half)

    return y[-1]


# ----------------------------------------------------------------------------------------------------------------------
# Beispielrechnung:
# ----------------------------------------------------------------------------------------------------------------------

def f(x, y):
    return x ** 2 / y


if __name__ == '__main__':
    quiver_plot(f, -2, 2, -2, 4, 0.25, 0.25)
    solution = mittelpunkt_verfahren(f, 0, 1.4, 2, 2)

    x_scale = np.arange(-2, 2, 0.15)
    exact = np.sqrt((2 * x_scale ** 3) / 3 + 4)
    plt.plot(1.4, solution, 'o', color='red')
    plt.plot(x_scale, exact)
    plt.show()
