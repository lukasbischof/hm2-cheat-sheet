# Symbolisch Rechnen mit Python

### Allgemeine Verwendung

#### Import

```python
import sympy as sp
```

#### Symbols

```python
x, y, z = sp.symbols('x y z')
```

#### Rechnen

```python
def f(y, z):
    return sp.exp(y) - sp.sin(z) + y ** 2
```

Variabeln substituieren:

```python
print(f(y, z).subs(y, 4))
```

#### Auswerten

```python
print(f(y, z).subs(y, 2).subs(z, 4).evalf())
```

### Matrizen und Jacobi-Matrix

```python
f1 = x ** 2 + ...
f2 = x ** 4 + ...

f = sp.Matrix([f1, f2])
X = sp.Matrix([x, y, z])
Df = f.jacobian(X)
print(Df) # ==> Jacobi-Matrix
```

Die Jacobi-Matrix hat gemäss Definition folgende Form:

$$
Df(x)=\begin{bmatrix}
\frac{df_1}{dx_1}\ \frac{df_1}{dx_2}\ \ldots\ \frac{df_1}{dx_n} \\
\frac{df_2}{dx_1}\ \frac{df_2}{dx_2}\ \ldots\ \frac{df_2}{dx_n} \\
\vdots \\
\frac{df_m}{dx_1}\ \frac{df_m}{dx_2}\ \ldots\ \frac{df_m}{dx_n}
\end{bmatrix}
$$

Danach können Variabeln substituiert werden:
```python
Df0 = Df.subs([(x, 3), (y, 4), (z, 5)]).evalf()
```

Oft wird auch eine Funktion generiert:

```python
import numpy as np

func = sp.lambdify([(x, y, z)], f, "numpy")
jac = sp.lambdify([(x, y, z)], Df, "numpy")

# Beispiel-Aufruf
print(jac(np.array([7, 8, 9])))
```
