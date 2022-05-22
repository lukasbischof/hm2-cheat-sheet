# Ausgleichsrechnung

* #### [➥ Lagrange](./lagrange)
* #### [➥ (Kubische) Splines](./splines)
* #### [➥ Lineare Ausgleichsprobleme](./lineare%20ausgleichsprobleme)
* #### [➥ Nichtlineare Ausgleichsprobleme](./nichtlineare%20ausgleichsprobleme)

### Interpolation: Problemstellung

Gegeben sind $n+1$ Wertepaare $(x_i,\ y_i),\text{ mit }i = 0,...,n$, mit $x_i\ \ne\ y_i$ für $i\ \ne\ j$. Gesucht ist eine stetige
Funktion $g$ mit der Eigenschaft $g(x_i) = y_i$, für alle $i=0,...,n$.

### Ausgleichsrechnung: Problemstellung

Im Unterschied zur Interpolation versuchen wir bei der Ausgleichsrechnung nicht, eine Funktion $f$ zu finden, die exakt
durch sämtliche $n$ Datenpunkte geht, sondern diese möglichst gut approximiert. Dabei ist bei der linearen
Ausgleichsrechnung die gesuchte Funktion $f(x)$
eine Linearkombination von $m$ sogenannten Basis-Funktionen $f_i(x)\ \text{(mit }i\ =\ 1,\ 2,\ \ldots,\ m\text{ und }m\ \leq\ n)$, d.h. die
gesuchten Parameter $λ_i$ treten nur als multiplikative Faktoren bzw. als Koeffizienten der Linearkombination auf.

![image](https://user-images.githubusercontent.com/8350985/123524284-7be04d00-d6c9-11eb-9721-9d280c1b7553.png)
