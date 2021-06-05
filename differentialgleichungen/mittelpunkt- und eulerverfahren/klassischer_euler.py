import numpy as np
import matplotlib.pyplot as plt


def euler_verfahren(f, a, b, n, y0):
    y = np.zeros(n + 1)
    y[0] = y0
    h = (b - a) / n
    x = np.append(np.arange(a, b, h), b)

    for i in range(1, n + 1):
        y[i] = y[i - 1] + h * f(x[i - 1], y[i - 1])

    return y[-1]


# ----------------------------------------------------------------------------------------------------------------------
# Beispielrechnung:
# ----------------------------------------------------------------------------------------------------------------------

def f(x, y):
    return x ** 2 / y


if __name__ == '__main__':
    solution = euler_verfahren(f, 0, 1.4, 2, 2)

    x_scale = np.arange(-2, 2, 0.15)
    exact = np.sqrt((2 * x_scale ** 3) / 3 + 4)
    plt.plot(1.4, solution, 'o', color='red')
    plt.plot(x_scale, exact)
    plt.grid(True)
    plt.title('Klassisches Euler-Verfahren')
    plt.show()
