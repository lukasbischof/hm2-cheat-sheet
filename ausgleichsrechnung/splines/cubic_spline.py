import numpy as np


def cubic_spline(x, y, xx):
    """
    Berechnet die natürlichen kubischen Splines für Stützpunkte x und y für gegebene x-Werte

    :param x: Die bekannten x-Werte der Stützpunkte
    :param y: Die bekannten y-Werte der Stützpunkte
    :param xx: Eine Liste mit x-Werten, für welche interpoliert werden soll.
    :return: y-Werte der Polynome für die gegebenen `xx`
    """
    if np.shape(x) != np.shape(y):
        raise Exception("shape mismatch")

    # Initialization
    n = len(x) - 1
    a = np.copy(y)[:-1]
    c = np.zeros(n + 1)

    A, h = calculate_matrix(x)

    z = 3 * ((y[2:n + 1] - y[1:n]) / h[1:n] - (y[1:n] - y[0:n - 1]) / h[0:n - 1])
    c[1:n] = np.linalg.solve(A, z)

    b = np.zeros(n)
    d = np.zeros(n)
    for i in range(0, n):
        b[i] = ((y[i + 1] - y[i]) / h[i]) - (h[i] / 3) * (c[i + 1] + 2 * c[i])
        d[i] = (1 / (3 * h[i])) * (c[i + 1] - c[i])

    return eval_polynom(a, b, c, d, x, xx)


def eval_polynom(a, b, c, d, x, xx):
    yy = np.copy(xx)
    for i in range(len(yy)):
        x_value = yy[i]
        index = next(j for j, v in enumerate(x) if v > x_value) - 1
        if index < 0:
            continue

        yy[i] = a[index] \
                + b[index] * (x_value - x[index]) \
                + c[index] * (x_value - x[index]) ** 2 \
                + d[index] * (x_value - x[index]) ** 3
    return yy


def calculate_matrix(x):
    n = len(x) - 1
    h = x[1:] - x[:-1]
    A = np.zeros((n - 1, n - 1))

    for i in range(n - 1):
        A[i, i] = 2 * (h[i] + h[i + 1])

    for i in range(0, n - 2):
        A[i, i + 1] = h[i]
        A[i + 1, i] = h[i]

    return A, h


# ----------------------------------------------------------------------------------------------------------------------
# Beispielrechnung:
# ----------------------------------------------------------------------------------------------------------------------

if __name__ == '__main__':
    x = np.array([4, 6, 8, 10])
    y = np.array([6, 3, 9, 0])

    x_range = np.arange(4, 10, 0.1)
    y_values = cubic_spline(x, y, x_range)

    import matplotlib.pyplot as plt

    plt.plot(x_range, y_values)         # Kubische Splines plotten
    plt.plot(x, y, 'o', label='data')   # Stützwerte plotten
    plt.grid(True)
    plt.title('Kubische Splines')
    plt.show()
