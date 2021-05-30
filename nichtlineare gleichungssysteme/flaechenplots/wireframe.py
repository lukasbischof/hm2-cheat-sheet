import matplotlib.pyplot as plt
import numpy as np

g = 9.81
R = 8.31


def W(v_0, alpha):
    return (v_0 ** 2 * np.sin(2 * alpha)) / g


def p(V, T):
    return (R * T) / V


if __name__ == '__main__':
    [V, T] = np.meshgrid(np.linspace(0, 0.2), np.linspace(0, 1e4))
    z = p(V, T)

    fig = plt.figure(4)
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_wireframe(V, T, z)

    plt.title('Gitter')
    plt.contour(V, T, z)
    ax.set_xlabel('V')
    ax.set_ylabel('T')
    ax.set_zlabel('W')

    plt.show()
