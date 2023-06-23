= Support Vector Machines (SVM)

Planteamos un problema de clatificación donde se tiene N muestras con M variables inedependientes; la variables depenientes podran tomar valores de {-1, 1}

Limite de deciscón: Linea conlindante con una parte del dataset

Las MVS sirven para aumentar el "hancho de las caretera"

Caso 1:Hard margin

Se tiene una margin muy estricta

La ecuacuón de la recta generada será: W \* X -b = 0

De modmo que la ecuación del hyperplano será

$$
W^{(1)} X^{(1)} + W^{(2)} X^{(2)} +W^{(m)} X^{(m)} - b = 0
$$

Vector unitario en dirección W

Si x está sobre el limite de decisión

$$
\frac{W}{||W||}
$$

Desplazamos un distancia D en dirección del usuario

$$
W + (X + d \frac{w}{||w||}) - b = 1
$$

$$
W * X - b + d \frac{w}{||w||}) = 1
$$

$$
d = \fra{1}{||w||}
$$

$$
margen = \frac{2}{||w||}
$$

Esta minimización de $||w||$ debe cumplir las siguientes restricciones:

$$
Si y_{(1)} = 1 esto implica que W X_1- b \leq 1
$$

$$
Si y_{(1)} = -1 esto implica que W X_1- b \gte -1
$$

$$
y_i(W X_i - b) \leq 1
$$

Esto será valido para todo i hasta n

Los vectores de soporte x_i cumplen

$$
y_i(W X_i - b) = 1
$$

Esta solución es mejor cuando son "pocos datos"

Caso 2: Soft Margin

Para este método usamos una función de perdidaa

Función de Perdida:

Hinge Loss (Perdida Bisagra)

$$
max(0, 1 - y_i(W X_i - b))
$$

Ejemplos

Caso #1:
$$
max(0, 1 - 1(\gt 1)) = 0
$$

Caso #2:
$$
max(0, 1 + 1(\lt -1)) = 0
$$

Caso #3:
$$
max(0, 1 + 1(\gt 1)) \gt 2.1
$$

Caso #4:
$$
max(0, 1 + 1(\gt -1 \lt 0)) \gt 0 \lt 1
$$

Una vez se ha indentificado la perdida se una función para minimizar la perdida de manera tal que:


$$
Min(w, b) \frac{1}{N} \sum_{i=1}^{N} max(0, y_i(w x_i - b)) + \lambda ||w||
$$

$$
Ese lambda será el que tan importante es maximizar la margen
$$
