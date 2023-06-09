from params import HIDDEN_LAYERS, OUTPUT_LAYERS, DATA_DIR, TRAIN_DATA_DIR
from utilities import read_numpy_like_json
from anns.neuronal_network import Simple


# Keeping data
train_metrics = read_numpy_like_json(f"{TRAIN_DATA_DIR}train.json")
print(train_metrics)

nn = Simple(num_inputs, HIDDEN_LAYERS, OUTPUT_LAYERS)

X_test_validation = np.load(f"{DATA_DIR}X_test_validation.npy", X_test_validation)
y_test_validation = np.load(f"{DATA_DIR}y_test_validation.npy", y_test_validation)
X_validation = np.load(f"{DATA_DIR}X_validation.npy", X_validation)
y_validation = np.load(f"{DATA_DIR}y_validation.npy", y_validation)
X_test = np.load(f"{DATA_DIR}X_test.npy", X_test)
y_test = np.load(f"{DATA_DIR}y_test.npy", y_test)

y_pred_train = nn.predict(X_train)
train_accuracy = np.mean(y_pred_train == y_train.reshape(-1, 1))
print(f"Training Accuracy: {train_accuracy * 100:.2f}%")

y_pred_test = nn.predict(X_test)
test_accuracy = np.mean(y_pred_test == y_test.reshape(-1, 1))
print(f"Test Accuracy: {test_accuracy * 100:.2f}%")
