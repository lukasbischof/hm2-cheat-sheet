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

```
        ⎡df1/dx1 df1/dx2 ... df1/dxn⎤
Df(x) = |df2/dx1 df2/dx2 ... df2/dxn|
        ⎣dfm/dx1 dfm/dx2 ... dfm/dxn⎦
```

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
