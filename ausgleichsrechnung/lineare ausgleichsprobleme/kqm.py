import numpy as np
import matplotlib.pyplot as plt


def kqm(X, Y, functions):
    """
    Berechnet die Koeffizienten Theta der Ansatzfunktion, welche eine Linearkombination aus
    f(x) = θ_1 * f_1(x) + θ_2 * f_2(x) + ... + θ_n * f_n(x)
    ist so, dass die Fehlerquadrate minimal werden, gemessen an gegebenen Stützstellen

    :param X: X-Werte der Stützstellen
    :param Y: Y-Werte der Stützstellen
    :param functions: Eine Liste mit den Funktionen f_1, f_2, ..., f_n
    :return: Eine Liste mit Koeffizienten zu den gegebenen Funktionen
    """

    assert len(X) == len(Y) and len(functions) > 0

    m, n = len(functions), len(X)
    A = np.zeros((n, m))
    for i in range(n):
        A[i] = np.array([f(X[i]) for f in functions])

    Q, R = np.linalg.qr(A)
    return np.linalg.solve(R, np.transpose(Q) @ Y)


# ----------------------------------------------------------------------------------------------------------------------
# Beispielrechnung:
#
# Visualisierung und Prognose der Prozessorentwicklung / Moore'sches Gesetz
# ----------------------------------------------------------------------------------------------------------------------


def f1(_x):
    return 1


def f2(x):
    return x - 1970


def f(theta):
    return lambda x: np.power(10, theta[0] * f1(x) + theta[1] * f2(x))


if __name__ == '__main__':
    data = np.array([
        [1971, 2250.],
        [1972, 2500.],
        [1974, 5000.],
        [1978, 29000.],
        [1982, 120000.],
        [1985, 275000.],
        [1989, 1180000.],
        [1989, 1180000.],
        [1993, 3100000.],
        [1997, 7500000.],
        [1999, 24000000.],
        [2000, 42000000.],
        [2002, 220000000.],
        [2003, 410000000.],
    ])

    X, Y = data[:, 0], data[:, 1]
    Y_log = np.log10(Y)

    thetas = kqm(X, Y_log, [f1, f2])

    # Visualisierung

    plt.semilogy(X, Y, 'o')
    plt.plot(X, f(thetas)(X))
    plt.xlabel('Jahr')
    plt.ylabel('Transistoren')
    plt.grid(True)
    plt.show()

    # Interpolation
    z11 = f(thetas)(2015)
    print(f'Z13 von IBM in 2015: {z11} (Grössenordnung 10^{int(np.log10(z11))})')

    # Prognose
    print(f'Thetas: {thetas}')
    print(f'Verdopplungszeit: {np.log10(2) / thetas[1]}')
    # Es ergibt sich ein exponentielles Wachstum mit theta 2 im Exponent
