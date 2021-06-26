# Lagrange Interpolationsformel

![image](https://user-images.githubusercontent.com/8350985/120298517-73634500-c2ca-11eb-89fe-cfac8741a788.png)
![image](https://user-images.githubusercontent.com/8350985/120299669-80ccff00-c2cb-11eb-8e02-a477b3ec202e.png)

### Beispiel

Gegeben sind folgende Messungen:

<img src="https://user-images.githubusercontent.com/8350985/123523830-b0063e80-d6c6-11eb-85ad-6e6e9f4bb9be.png" width="45%">

Das ergiebt `n + 1 = 4` Stützpunkte, also ist `n = 3`. 
Das Interpolationspolynom hat also die Form

<img src="https://user-images.githubusercontent.com/8350985/123523861-f8bdf780-d6c6-11eb-94b7-d8037a983141.png" width="75%">

Die Lagrangepolynome berechnen sich folgendermassen:

![image](https://user-images.githubusercontent.com/8350985/123523876-18552000-d6c7-11eb-8b39-da647fe94729.png)
<img src="https://user-images.githubusercontent.com/8350985/123523957-8ac60000-d6c7-11eb-8215-551359826490.png" width="85%">

## Fehlerabschätzung

![image](https://user-images.githubusercontent.com/8350985/123523741-ee4f2e00-d6c5-11eb-9c2e-fa6859708fef.png)

Die Fehlerabschätzung ist also nur anwendbar, wenn wir die Funktion `f(x)` bzw. ihre Ableitungen selbst kennen. 
Deshalb ist diese Fehlerabschätzung theoretischer Natur.
