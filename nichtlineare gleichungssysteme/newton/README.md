# Newton-Verfahren

Gesucht sind Nullstellen von `f: ℝ^n ⟼ ℝ^n` mit einem Bekannten `x0` in der Nähe einer Nullstelle.
Das Newton-Verfahren lautet dann:

Für n=1,...,n:
* Sei 𝜹_n die Lösung des Gleichungssystems `Df(x_n) * 𝜹_n = -f(x_n)` 
* `x_{n+1} := x_n + 𝜹_n`
