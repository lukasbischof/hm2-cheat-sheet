import numpy as np


def trapez(x, y):
    """
    Implementation der Trapez Regel für eine Liste von Funktionsauswertungen.

    :param x: X-Werte der Funktionsauswertungen, sortiert
    :param y: Y-Werte der Funktionsauswertungen, in der selben Reihenfolge wie die dazugehörigen X-Werte
    :return: Das Integral von min(x) bis max(x) über y
    """
    assert len(x) == len(y)
    n = len(x)
    res = 0

    for i in range(n - 1):
        res = res + ((y[i] + y[i + 1]) / 2) * (x[i + 1] - x[i])
    return res


# ----------------------------------------------------------------------------------------------------------------------
# Beispielrechnung:
# ----------------------------------------------------------------------------------------------------------------------

r = [0, 800, 1200, 1400, 2000, 3000, 3400, 3600, 4000, 5000, 5500, 6370]
rho = [13000, 12900, 12700, 12000, 11650, 10600, 9900, 5500, 5300, 4750, 4500, 3300]

if __name__ == '__main__':
    x = [x * 1000 for x in r]
    y = [y * 4 * np.pi * x[i] ** 2 for i, y in enumerate(rho)]

    calculated = trapez(x, y)
    real = 5.9722e24
    print(f'Berechnet: {calculated}')
    print(f'Real: {real}')
    # > 6.02609577351443e+24

    print(f'Absoluter Fehler: {np.abs(real - calculated)}')
    print(f'Relativer Fehler: {np.abs(real - calculated) / real}')
