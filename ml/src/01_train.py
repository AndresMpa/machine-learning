from params import LEARNING_RATE, DATA_DIR, TEST_PERCENTAGE, VALIDATION_PERCENTAGE, HIDDEN_LAYERS, OUTPUT_LAYERS, EPOCHS
from sklearn.model_selection import train_test_split
from anns.neuronal_network import Simple
import numpy as np

x_inputs = np.load(f"{DATA_DIR}inputData.npy")
y_expected = np.load(f"{DATA_DIR}outputData.npy")

X_train, X_test_validation, y_train, y_test_validation = train_test_split(
    x_inputs, y_expected, test_size=TEST_PERCENTAGE+VALIDATION_PERCENTAGE)

X_validation, X_test, y_validation, y_test = train_test_split(
    X_test_validation, y_test_validation, test_size=TEST_PERCENTAGE)

num_inputs = X_train.shape[1]

nn = Simple(num_inputs, HIDDEN_LAYERS, OUTPUT_LAYERS)
nn.train(X_train, y_train, epochs=EPOCHS, lr=LEARNING_RATE)

y_pred_train = nn.predict(X_train)
train_accuracy = np.mean(y_pred_train == y_train.reshape(-1, 1))
print(f"Training Accuracy: {train_accuracy * 100:.2f}%")

y_pred_test = nn.predict(X_test)
test_accuracy = np.mean(y_pred_test == y_test.reshape(-1, 1))
print(f"Test Accuracy: {test_accuracy * 100:.2f}%")
