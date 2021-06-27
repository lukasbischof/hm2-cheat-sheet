# Lineare Ausgleichsprobleme

![image](https://user-images.githubusercontent.com/8350985/123544252-b215df00-d752-11eb-96f5-0ff5251079a0.png)

Man kann nun versuchen, das Fehlerfunktional zu minimieren. 
Dazu muss die partielle Ableitung `∂E(f) / ∂𝝀_j` null sein, was zur Normalengleichung führt:

![image](https://user-images.githubusercontent.com/8350985/123544263-bfcb6480-d752-11eb-9ee3-8cc0588a550e.png)

Die Lösung von A transponiert ist allerdings häufig schlecht konditioniert, weshalb das Lösen mithilfe einer
QR-Zerlegung (numerisch) effizienter ist.

![image](https://user-images.githubusercontent.com/8350985/120321212-525b1e00-c2e3-11eb-85a4-cb2930e0e549.png)

Aus `A = QR` folgt also für das Normalengleichungssystem also `R𝝀 = Q^T · y`, welches besser konditioniert ist.

## Beispiel

<img src="https://user-images.githubusercontent.com/8350985/123544852-995af880-d755-11eb-9b82-dbe595d134c4.png" width="80%">
