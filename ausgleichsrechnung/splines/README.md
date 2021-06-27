# Splineinterpolation 

![image](https://user-images.githubusercontent.com/8350985/123524134-7cc4af00-d6c8-11eb-8ef0-1d795e8cbd5f.png)

Das Gleichungssystem unter Punkt 4 hat dabei folgende Form:

![image](https://user-images.githubusercontent.com/8350985/123541071-b508d380-d742-11eb-88db-8c38287f815c.png)

Dies kann in Python folgendermaßen generiert werden:

```python
import numpy as np

def calculate_matrix(x):
    n = len(x) - 1
    h = x[1:] - x[:-1]
    A = np.zeros((n - 1, n - 1))

    for i in range(n - 1):
        A[i, i] = 2 * (h[i] + h[i + 1])

    for i in range(0, n - 2):
        A[i, i + 1] = h[i]
        A[i + 1, i] = h[i]

    return A, h
```

## Beispiel

![image](https://user-images.githubusercontent.com/8350985/123524117-67e81b80-d6c8-11eb-88db-60fcda0b48af.png)

![image](https://user-images.githubusercontent.com/8350985/123540817-2e072b80-d741-11eb-9cf9-bd2de0451902.png)
