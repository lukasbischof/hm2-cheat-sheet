import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm

g = 9.81
R = 8.31


def W(v_0, alpha):
    return (v_0 ** 2 * np.sin(2 * alpha)) / g


def p(V, T):
    return (R * T) / V


if __name__ == '__main__':
    [v_0, alpha] = np.meshgrid(np.linspace(0, 100), np.linspace(0, np.pi / 2))
    z = W(v_0, alpha)

    fig = plt.figure(4)
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_wireframe(v_0, alpha, z)
    ax.plot_surface(v_0, alpha, z, cmap=cm.coolwarm, linewidth=0, antialiased=True)

    plt.title('Gitter')
    plt.contour(v_0, alpha, z)
    ax.set_xlabel('v_0')
    ax.set_ylabel('alpha')
    ax.set_zlabel('W')

    plt.show()
