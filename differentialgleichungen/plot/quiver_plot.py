import numpy as np
import matplotlib.pyplot as plt


def quiver_plot(f, xmin, xmax, ymin, ymax, hx, hy):
    X = np.arange(xmin, xmax, hx)
    Y = np.arange(ymin, ymax, hy)
    xv, yv = np.meshgrid(X, Y)

    plt.quiver(X, Y, np.ones(np.shape(xv)), f(xv, yv))
    plt.grid(True)
    plt.xlabel('x')
    plt.ylabel('y\'(x)')


# ----------------------------------------------------------------------------------------------------------------------
# Beispielrechnung:
# ----------------------------------------------------------------------------------------------------------------------


def f(x, y):
    return x ** 2 / y


if __name__ == '__main__':
    quiver_plot(f, -2, 2, -2, 2, 0.5, 0.5)
    plt.show()
