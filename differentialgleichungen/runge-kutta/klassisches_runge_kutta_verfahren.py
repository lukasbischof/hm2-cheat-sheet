import numpy as np


def classic_runga_kutta(f, a, b, n, y0):
    y = np.zeros(n + 1, dtype=np.float64)
    y[0] = y0
    h = (b - a) / n
    x = np.append(np.arange(a, b, h, dtype=np.float64), b)
    for i in range(1, n + 1):
        h_2 = h / 2
        k1 = f(x[i - 1], y[i - 1])
        k2 = f(x[i - 1] + h_2, y[i - 1] + (h_2 * k1))
        k3 = f(x[i - 1] + h_2, y[i - 1] + h_2 * k2)
        k4 = f(x[i - 1] + h, y[i - 1] + h * k3)
        y[i] = y[i - 1] + h * (1 / 6) * (k1 + 2 * k2 + 2 * k3 + k4)
    return x, y


# ----------------------------------------------------------------------------------------------------------------------
# Angepasstes Runge-Kutta Verfahren:
# ----------------------------------------------------------------------------------------------------------------------

'''
Gewählter 4-stufiger Runge-Kutta Verfahren der Form:
c1 |
c2 | a21 |
c3 | a31 | a32 |
c4 | a41 | a42 | a43 |
---|-----|-----|-----|----
b  | b1  | b2  | b3  | b4

hier:

0    |
0.75 | 0.5  |
0.5  | 0.25 | 0.5  |
0.25 | 0    | 0.25 | 1    |
-----|------|------|------|----
b    | 2/10 | 3/10 | 3/10 | 2/10

Mit c1=0, c2=0.75, c3=0.5, c4=0.25
    b1=2/10, b2=3/10, b3=3/10, b4=2/10
    a21=0.5
    a31=0.25, a
'''


def custom_runge_kutta(f, a, b, n, y0):
    y = np.zeros(n + 1, dtype=np.float64)
    y[0] = y0
    h = (b - a) / n
    x = np.append(np.arange(a, b, h, dtype=np.float64), b)
    for i in range(1, n + 1):
        k1 = f(x[i - 1], y[i - 1])
        k2 = f(x[i - 1] + 0.75 * h, y[i - 1] + h * (0.5 * k1))
        k3 = f(x[i - 1] + 0.5 * h, y[i - 1] + h * (0.25 * k1 + 0.5 * k2))
        k4 = f(x[i - 1] + 0.25 * h, y[i - 1] + h * (0.25 * k2 + k3))
        y[i] = y[i - 1] + h * (0.2 * k1 + 0.3 * k2 + 0.3 * k3 + 0.2 * k4)
    return x, y


# ----------------------------------------------------------------------------------------------------------------------
# Beispielrechnung:
# ----------------------------------------------------------------------------------------------------------------------

def f(x, y):
    return x ** 2 + 0.1 * y


if __name__ == '__main__':
    print(Bischof_S12_Aufg1(f, -1.5, 1.5, 5, 0))
