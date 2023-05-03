Se llegó a que:

$$
J(\theta) = \frac{1}{2N} (\theta^{T} X^{T} X\theta - 2y^{t} X \theta + y^{T} y)
$$

> Esta es la función de perdida, la idea es hallar los $\theta$ que minimcen el error

1) Para eso se usa la derivada de:

$$
\frac{\partial \theta^{T} X^{T} X\theta }{\partial \theta}
$$

$$
X^T X = A
$$

Esto será una matriz cuadrada

$$
f(\theta) = \theta^T A \theta
$$

$$
\frac{\partial f}{\partial \theta} = 2A\theta
$$

2) Ahora se usa la derivada de:

$$
\frac{\partial 2y^{T} X\theta }{\partial \theta} = 2y^TX
$$

3) Ahora se deriva:

$$
\frac{\partial y^Ty}{\partial \theta} = 0
$$

$$
\frac{\partial J(\theta)}{\partial \theta} = \frac{1}{2N}(2X^TX\theta - 2(y^TX)^T)
$$

$$
\frac{\partial J(\theta)}{\partial \theta} = \frac{1}{N}(X^TX\theta-X^Ty) = 0
$$

$$
X^TX \theta = X^Ty
$$

Por tanto la forma de encontrar el $\theta$ que minimiza $J(\theta)$ será:

Esto se conoce como el gradiente positivo

$$
\therefore  \theta = (X^TX)^{-1}X^Ty
$$

Compuacionalmente hablando esta función escala cuadraticamente, es decir; se hace inviable porque la complejidad computacional escala de manera cuadratica

> Basicamente esta función se usa para coger todos los puntos del plano n dimensional y arrojar el valor minimo de $J(\theta)$ lo cual es demasiado costo computacionalmente hablando, pues tendría que calcular todo el espacio

Esto se conoce como el gradiente negativo

$$
\theta = \theta - \eta \partial \theta
$$

Donde:

- $\eta$ es el learning rate (Tasa de aprendizaje)

Ref: https://www.hiberus.com/crecemos-contigo/analisis-de-componentes-principales/
