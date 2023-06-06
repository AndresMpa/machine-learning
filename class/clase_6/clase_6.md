# Clase 6

Con la librería `time` se puede determinar el tiempo que tarda en optimizar un algoritmo de cualquier cosa

## Gradiente

El gradiente es una vector que indica hacía adonde se da la mayor taza de cambio

```
f(w) = 2w
f'(w) = ?

f'(w) = 2w

f'(w) = 0

2w = 0
w = 0
```

La idea es identificar el `w` en `f(w)` en donde es minimo (loss)

Donde $\eta$ es la tasa de aprendizaje

$$
w := w - η f'(w)
$$

Si usamos la función de loss (Costo):

$$
J(\theta) = \frac{1}{2N} \sum{(\hat{y} - y)^{2}} ; \hat{y} = \theta_1 X + \theta_2 x^{2}
$$
