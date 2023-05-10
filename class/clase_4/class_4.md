# Regresión polinomial

La diferencia es que permite caracterizar datos que son no lineales de modo que:

$$
h_{\theta}(X) = \theta_0 X + \theta_1 X^2
$$

Como sigue siendo lineal con respecto a $\theta$ significa que sigue siendo una regresión lineal en donde las entradas tiene un comportamiento polinomia, en este caso cuadratico

> ¿Como visualizar si el error es tan chico o grande como tengo esperado?

## ¿Qué hago cuando lo veo en número y no en graficos?

Para calcular la perdida se usa el MSE (Recordar que está en una escala diferente a los datos), para hacer el ajuste se usa la raíz cuadrada:

$$
rmse = np.sqrt(np.mena((y_predcit - y)**2))
print(f"RMSE: {rmse}")
$$

## MSE vs MAE

La mayor diferencia entre el RMSE y el MAE es que el MSE es diferenciable mientras el MAE no es diferenciable en 0. Basicamente es mejor en el valor de 0

MSE castiga mucho las diferencias grande, entre más grande sea la diferencia más grande será su valor por lo que esto complica el calculo

MAE funciona sobre valor absoluto esto me permite obviar ese "castigo" sobre las grande diferencias

> Generalmente se saca un histograma, diagramas, etc... De forma estadistica de los datasets
