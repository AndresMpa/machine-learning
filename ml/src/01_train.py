from params import LEARNING_RATE, DATA_DIR, TEST_PERCENTAGE, VALIDATION_PERCENTAGE, HIDDEN_LAYERS, OUTPUT_LAYERS, EPOCHS, TRAIN_DATA_DIR
from sklearn.model_selection import train_test_split
from anns.neuronal_network import Simple
from utilities import write_file
import numpy as np

# Getting data from storage
x_inputs = np.load(f"{DATA_DIR}inputData.npy")
y_expected = np.load(f"{DATA_DIR}outputData.npy")

# Splitting sets
X_train, X_test_validation, y_train, y_test_validation = train_test_split(
    x_inputs, y_expected, test_size=TEST_PERCENTAGE+VALIDATION_PERCENTAGE)

X_validation, X_test, y_validation, y_test = train_test_split(
    X_test_validation, y_test_validation, test_size=TEST_PERCENTAGE)

# Creating Neuronal Network
num_inputs = X_train.shape[1]

nn = Simple(num_inputs, HIDDEN_LAYERS, OUTPUT_LAYERS)
nn.train(X_train, y_train, epochs=EPOCHS, lr=LEARNING_RATE)

# Getting metrics
metrics = nn.get_loss()

metrics_data = {
    "loss": metrics[0],
    "number_of_inputs": num_inputs,
    "size": metrics[1]
}

# Keeping data
write_file(metrics_data, TRAIN_DATA_DIR, "train.json")

np.save(f"{DATA_DIR}X_test_validation.npy", X_test_validation)
np.save(f"{DATA_DIR}y_test_validation.npy", y_test_validation)
np.save(f"{DATA_DIR}X_validation.npy", X_validation)
np.save(f"{DATA_DIR}y_validation.npy", y_validation)
np.save(f"{DATA_DIR}X_test.npy", X_test)
np.save(f"{DATA_DIR}y_test.npy", y_test)
