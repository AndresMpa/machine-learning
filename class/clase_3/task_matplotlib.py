import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('./winequality-white.csv', sep=";")

y = df["quality"].values.reshape(-1, 1)

X_volatile = df['volatile acidity'].values.reshape(-1, 1)
X_tsd = df['total sulfur dioxide'].values.reshape(-1, 1)
X_fsd = df['free sulfur dioxide'].values.reshape(-1, 1)
X_acidity = df['fixed acidity'].values.reshape(-1, 1)
X_sugar = df['residual sugar'].values.reshape(-1, 1)
X_sulphates = df['sulphates'].values.reshape(-1, 1)
X_chlorides = df['chlorides'].values.reshape(-1, 1)
X_acid = df['citric acid'].values.reshape(-1, 1)
X_density = df['density'].values.reshape(-1, 1)
X_alcohol = df['alcohol'].values.reshape(-1, 1)
X_pH = df['pH'].values.reshape(-1, 1)

X_tags = [
    X_volatile,
    X_tsd,
    X_fsd,
    X_acidity,
    X_sugar,
    X_sulphates,
    X_chlorides,
    X_acid,
    X_density,
    X_alcohol,
]

X = X_pH


for tag in X_tags:
    np.hstack([tag, X])

print(X, end='\n')


