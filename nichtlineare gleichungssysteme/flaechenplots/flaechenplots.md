# Zweidimensionale Flächen darstellen

1. Erstellen von einem 3D Meshgrid/Koordinatennetz:

```python
import numpy as np
import matplotlib.pyplot as plt

[x, y] = np.meshgrid(np.linspace(-5, 5), np.linspace(-5, 5))
```

2. Definition der Z-Achse

```python
def f(x):
    ...

z = f(x, y)
```

3. Rendern des Plots

```python
fig = plt.figure(1)
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(x, y, z)

plt.title('Fläche')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')

plt.show()
```
