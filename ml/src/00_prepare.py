from sklearn.datasets import make_circles
import numpy as np
import os

OUTPUT_DIR = 'data/'
os.makedirs(OUTPUT_DIR, exist_ok=True)

# To generated equivalent data under a seed
np.random.seed(0)

x_inputs, y_spected = make_circles(n_samples=200, noise=0.05)

# Storage data as numpy arrays
np.save('data/inputData.npy', x_inputs)
np.save('data/outputData.npy', y_spected)
