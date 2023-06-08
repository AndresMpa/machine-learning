from sklearn.datasets import make_circles
from utilities import handle_directory
from params import DATA_DIR
import numpy as np
import os

handle_directory(DATA_DIR)

# To generated equivalent data under a seed
np.random.seed(0)

x_inputs, y_expected = make_circles(n_samples=200, noise=0.05)

# Storage data as numpy arrays
np.save(f"{DATA_DIR}inputData.npy", x_inputs)
np.save(f"{DATA_DIR}outputData.npy", y_expected)
