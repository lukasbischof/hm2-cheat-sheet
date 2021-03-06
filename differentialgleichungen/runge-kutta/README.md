# Runge-Kutta Verfahren

## Klassisches vierstufiges Runge-Kutta Verfahren

![image](https://user-images.githubusercontent.com/8350985/120799891-96e2f580-c53f-11eb-998b-eec063e3b69f.png)

Das klassische vierstufige Runge-Kutta Verfahren hat die Konsistenz- und Konvergenzordnung `p = 4`.

## Allgemeines *s*-stufiges Runge-Kutta Verfahren

<img src="https://user-images.githubusercontent.com/8350985/120812311-2642d580-c54d-11eb-9ee7-60db9cd1cd24.png" width="80%">

Die Koeffizienten notiert man dabei meist in der Form:

<img src="https://user-images.githubusercontent.com/8350985/120906656-8e7fdd00-c65b-11eb-836e-8934b4a56462.png" width="50%">

Dabei kann man die Euler-Verfahren und das Mittelpunkt-Verfahren auf folgende Schemata zurückführen:

![image](https://user-images.githubusercontent.com/8350985/120906652-81fb8480-c65b-11eb-8d22-cd9f88e3b84a.png)

## Erweiterung auf Systeme von Differentialgleichungen

### Zurückführen einer DGL *k*-ter Ordnung auf *k* DGL 1. Ordnung

Durch Umformen können auch Differentialgleichungen höherer Ordnung gelöst werden. Dazu geht man wie folgt vor:

Für eine Differentialgleichung k-ter Ordnung:

1. Nach der höchsten vorkommenden (k-ten) Ableitung der unbekannten Funktion auflösen
2. Hilfsfunktionen `z_i` der unbekannten Funktion und deren Ableitungen einführen, bis zu `z_k(x) = y^(k-1)(x)`
3. Das System erster Ordnung durch Ersetzen der höheren Ableitungen durch die neuen Funktionen aufstellen
4. Differentialgleichung in vektorieller Form aufschreiben

#### Beispiel

<img src="https://user-images.githubusercontent.com/8350985/120817617-24c7dc00-c552-11eb-81b3-71fefbb251a4.png" width="80%">

### Lösen eines Systems von *k* Differentialgleichungen 1. Ordnung

![image](https://user-images.githubusercontent.com/8350985/123560404-2f1c7500-d7a2-11eb-98cf-2372dc5f0c98.png)
![image](https://user-images.githubusercontent.com/8350985/123560425-4a878000-d7a2-11eb-839b-1bb1db1eccc5.png)

#### Beispiel

Ausgehend vom oberen Beispiel:

![image](https://user-images.githubusercontent.com/8350985/123560530-06e14600-d7a3-11eb-8565-ef6a0585d264.png)

## Stabilität

In gewissen Situationen kann es vorkommen, dass der numerische Fehler unbegrenzt grösser werden kann,
unabhängig von der Schrittweite `h`. Man spricht dann von einer instabilen Lösung.

![image](https://user-images.githubusercontent.com/8350985/120906625-51b3e600-c65b-11eb-90d3-0f75e0f1bd50.png)

## Python-Funktionen für das Lösen von gewöhnlichen DGL

Das Scipy Paket stellt eine Funktion für das Lösen mittels Runge-Kutta Verfahren bereit:

```python
from scipy.integrate import solve_ivp


def exponential_decay(_t, y):
    return -0.5 * y


range = [0, 10]
initial_state = [2, 4, 8]
solution = solve_ivp(exponential_decay, range, initial_state)
```
