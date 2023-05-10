# Clasificación

Basicamente nos movemos de un valor continuo a un valor discreto, lo que se trata de definir es la pertenencia de la entrada a una salida.

## Regresión logistica

Definimos la función sigmoidal:

$$
\sigma(z) = \frac{1}{1+e^{-z}}
$$

Entonces podemos asumir el parametro z como una función lineal de manera que:

$$
z = w_0 + w_1x_1 + w_2x_2 + ... + w_nx_n
$$

$$
w_0 + \sum_{i=1}^{n}w_ix_i
$$

Para encontrar los w se usa la maxima verosimilitud, basicamente lo que hace es predecir que tna bien el modelo predice las clases verdaderas.

La verosimilitud está dada por la ecuación:

$$
L(w) = \prod_{i=1}^{m}P(y^{(i)} | x^{(i)}, w)
$$

Esta se conoce como la función de verosimilitud y esta sirve para calcular el error

> Hay que tener en cuenta que la variable dependiente es un etiqueta, es decir; la salida del modelo es un categoria, de modo que X de hecho es un vector de valores continuos

Para la clasificación se puede usar el logaritmo de esta función

## Cross entropy

Esto hace un calculo del logaritmo dependiendo de si el valor real es 0 o 1, si el valor real es 0, la siguiente ecuación se va 0

La entropia binaria cruzada, representa el error

$$
log(L(w)) = \sum_{i=1}^{m}[y^{(i)} * log(\hat{y}^{(i)}) + (1 - y^{(i)}) * log(1 - \hat{y}^{(i)})]
$$

Esta función se conoce como $BCE$ Binary Cross Entropy

$$
\hat{y}^{(j)} = \sigma(w_0 + \sum_{i=1}^{n}w_ix_i^{(j)} = \sigma(w_0 + WX^{(j)})
$$

Con $W$ y $X^{(j)}$ siendo vectores

Basicamente se puede entender la función de sigmoidal como una forma de llevar el calculo a la estadistica

| $y$ | $\hat{y}$ | $Log(\hat{y})$ | Treshold |
| --- | --------- | -------------- | -------- |
| $0$ | $0.1$     | $-0.046$       | VN       |
| $1$ | $0.9$     | $-0.046$       | VP       |
| $0$ | $0.9$     | $-1$           | FP       |
| $1$ | $0.1$     | $-1$           | FN       |

## Matriz de confusión

$$
\frac{2}{m}
\begin{pmatrix}
VN & FP \\
FN & VP
\end{pmatrix}
$$

Donde m corresponde con:
$$
m = VN + VP + FN + FP
$$

En el caso ideal esta matriz es una identidad

La suma de todos los valores da m, en el caso ideal FP y FN debe ser 0 en VN y VP será una identidad, en el caso ideal, VN y VP serán el mismo valor

> Para interpretar de forma correcta la matriz de confusión, es necesario saber que tan desbalanceado están los datos, %50 en VN y %50 en VP es el caso ideal

## Exactitud (Accuracy)

Se da de la siguiente forma:

El número de predicciones verdaderas: VN + VP
Sobre el total de las predicciones: m

$$
Accuracy=\frac{VN + VP}{m}
$$

Ejemplo, si este valor es igual a 0.9 eso significa que el 90% de las predicciones son verdaderas, es decir; el modelo es bueno

Esta metrica tiene un problema, si el dataset está desbalanceado, por ejemplo si tengo datos en donde el 90% del data set tiene VP y el modelo solo predice bien VP el accuracy tambien será del 90% pese a que fallaría todos los VN

> Esta metrica es engañosa

## Presición (Presicion)

$$
\frac{VP}{VP+FP}
$$

Esta metrica permite saber que porcentaje de los positivos es correcto, este es el porcentaje existoso de positivos sobre el total de positivos

## Exhautividad (Recall)

$$
\frac{VP}{VP+FN}
$$

Esto indica el porcentaje de verdaderos con respecto al total de positivos en el dataset

## Puntaje F1 (F1 Score)

$$
\frac{2 * Presicion * Recall}{Precision + Recall}
$$

Esta es la metrica menos susceptible a desbalanceo, su maximo valor es 1. Esta es una media geometrica

## Curva ROC (Reciving Operating Caractheristic)

Para usar el ROC se ha de sintonizar el Treshold (Recordar que el Treshold para todos estos calculos es de 0.5 de la función sigmoidal). Para diferences umbrales se calcula la taza de falsos positivos contra la taza de falsos negativos

## AU-ROC (AUC-ROC)

Esta es el area bajo la curva de ROC, el AU-ROC es otra metrica bastante util para medir que tan buena

## Precision-Recall curve (PR or PRC)

Es otra metica que usa la precision y el recall

## AU-PR or AUC-PR

Es lo mismo que el concepto anterior, pero con la curva PR
