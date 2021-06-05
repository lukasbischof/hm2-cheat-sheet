import numpy as np
from matplotlib import pyplot as plt


def mod_euler_verfahren(f, a, b, n, y0):
    """
    Berechnet die Lösung einer gegebenen Differentialgleichung mit dem modifizierten Euler-Verfahren.

    :param f: Die Differentialgleichung in der Form f(x, y)
    :param a: Der Anfangswert x_0
    :param b: Der X-Wert für die gesuchte Lösung
    :param n: Die Anzahl an Schritten, welche durchgeführt werden sollen.
              Je mehr Schritte, desto kleiner wird die Schrittweite und desto genauer das Resultat
    :param y0: Der Anfangswert y_0, welcher zusammen mit a den Startpunkt (a, y_0) bildet
    :return: Die gesuchte 1-D Lösung für y(a)
    """
    y = np.zeros(n + 1)
    y[0] = y0
    h = (b - a) / n
    x = np.append(np.arange(a, b, h), b)

    for i in range(1, n + 1):
        k1 = f(x[i - 1], y[i - 1])
        y1 = y[i - 1] + h * k1
        k2 = f(x[i], y1)
        y[i] = y[i - 1] + h * (k1 + k2) / 2

    return y[-1]


# ----------------------------------------------------------------------------------------------------------------------
# Beispielrechnung:
# ----------------------------------------------------------------------------------------------------------------------

def f(x, y):
    return x ** 2 / y


if __name__ == '__main__':
    solution = mod_euler_verfahren(f, 0, 1.4, 2, 2)

    x_scale = np.arange(-2, 2, 0.15)
    exact = np.sqrt((2 * x_scale ** 3) / 3 + 4)
    plt.plot(1.4, solution, 'o', color='red')
    plt.plot(x_scale, exact)
    plt.grid(True)
    plt.title('Modifiziertes Euler-Verfahren')
    plt.show()
