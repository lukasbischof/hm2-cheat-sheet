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
