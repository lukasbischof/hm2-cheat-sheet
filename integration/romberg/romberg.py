import numpy as np


def romberg(f, a, b, m):
    """
    :param f: Die Funktion f(x)
    :param a: Die Integrationsuntergrenze
    :param b: Die Integrationsobergrenze
    :param m: Die Extrapolationstiefe
    :return:
    """

    assert a != b

    T = initialize_romberg(a, b, f, m)

    for k in range(1, m + 1):
        for j in range(0, m - k + 1):
            factor = 4 ** k
            T[j][k] = (factor * T[j + 1, k - 1] - T[j, k - 1]) / (factor - 1)

    return T[0][m]


# noinspection PyPep8Naming
def initialize_romberg(a, b, f, m):
    T = np.zeros((m + 1, m + 1))
    outer = (f(a) + f(b)) / 2
    for j in range(0, m + 1):
        n = 2 ** j
        h = (b - a) / n
        s = sum(map(lambda i: f(a + h * i), list(range(1, n))))
        T[j][0] = h * (outer + s)

    return T


# ----------------------------------------------------------------------------------------------------------------------
# Beispielrechnung:
# ----------------------------------------------------------------------------------------------------------------------

def f(x):
    return np.cos(x ** 2)


if __name__ == '__main__':
    print(f'==> {romberg(f, 0, np.pi, 4)}')
