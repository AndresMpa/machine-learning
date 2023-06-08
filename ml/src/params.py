from utilities import get_params


TRAIN_PERCENTAGE = get_params("train_percentage")
VALIDATION_PERCENTAGE = get_params("validation_percentage")
TEST_PERCENTAGE = get_params("test_percentage")

HIDDEN_LAYERS = get_params("hidden_layers")
OUTPUT_LAYERS = get_params("output_layers")

LEARNING_RATE = get_params("learning_rate")
EPOCHS = get_params("epochs")

DATA_DIR = get_params("data_dir")
MODEL_DIR = get_params("model_dir")
