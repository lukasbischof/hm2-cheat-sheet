# Newton-Verfahren

![image](https://user-images.githubusercontent.com/8350985/123520758-8cd19400-d6b2-11eb-9fa5-f4f9dc07426e.png)

Es kann allerdings passieren, dass mit dem Newton-Verfahren ein lokales Minimum anstelle einer Nullstelle gefunden wird.

### Konvergenz

Das Newton-Verfahren konvergiert quadratisch für nahe genug an einer Nullstelle liegende Starvektoren, 
wenn `Df(x)` regulär und `f` dreimal stetig differenzierbar ist.

## Vereinfachtes Newton-Verfahren

Der Aufwand kann reduziert werden, wenn nicht bei jedem Schritt die Jacobi-Matrix ausgewertet werden muss:

![image](https://user-images.githubusercontent.com/8350985/123520827-14b79e00-d6b3-11eb-8012-937f15140408.png)

Das vereinfachte Verfahren **konvergiert allerdings nur noch linear**.

## Gedämpftes Newton-Verfahren

Falls beim *n*-ten Iterationsschritt die Jacobi-Matrix `Df(x_n)` schlecht konditioniert ist, 
kann generell nicht erwartet werden, dass ein weiterer Schritt eine bessere Näherung an die Nullstelle darstellt.

![image](https://user-images.githubusercontent.com/8350985/123520891-7972f880-d6b3-11eb-82a7-b940ee85a4a7.png)
