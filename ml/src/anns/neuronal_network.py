# OS dependencies
from params import MODEL_DIR
from utilities import write_file
import json
import codecs
import sys
import os

# ML dependencies
import matplotlib.pyplot as plt
import numpy as np

"""
To import upper level directories
"""
current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

# Upper level requirements


class Simple:
    def __init__(self, num_inputs, num_hidden, num_outputs):
        self.W1 = np.random.randn(num_inputs, num_hidden)
        self.b1 = np.zeros((1, num_hidden))
        self.W2 = np.random.randn(num_hidden, num_outputs)
        self.b2 = np.zeros((1, num_outputs))
        self.loss = []

    def set_weigths(W1, b1, W2, b2):
        self.W1 = W1
        self.b1 = b1
        self.W2 = W2
        self.b2 = b2

    def binary_cross_entropy(self, y, y_hat):
        m = y.shape[0]
        bce = -1 / m * np.sum(y * np.log(y_hat) + (1 - y) * np.log(1 - y_hat))
        return bce

    def binary_cross_entropy_gradient(self, y, y_hat):
        m = y.shape[0]
        bce_gradient = -1 / m * (y / y_hat - (1 - y) / (1 - y_hat))
        return bce_gradient

    def sigmoid(self, z):
        return 1 / (1 + np.exp(-z))

    def feedforward(self, X):
        z1 = np.dot(X, self.W1) + self.b1
        a1 = self.sigmoid(z1)
        z2 = np.dot(a1, self.W2) + self.b2
        y_hat = self.sigmoid(z2)
        return z1, a1, z2, y_hat

    def backpropagation(self, X, y, z1, a1, z2, y_hat):
        m = X.shape[0]
        dz2 = self.binary_cross_entropy_gradient(y, y_hat)
        dW2 = 1 / m * np.dot(a1.T, dz2)
        db2 = 1 / m * np.sum(dz2, axis=0)
        dz1 = np.dot(dz2, self.W2.T) * (a1 * (1 - a1))
        dW1 = 1 / m * np.dot(X.T, dz1)
        db1 = 1 / m * np.sum(dz1, axis=0)
        return dW1, db1, dW2, db2

    def update_parameters(self, dW1, db1, dW2, db2, lr):
        self.W1 -= lr * dW1
        self.b1 -= lr * db1
        self.W2 -= lr * dW2
        self.b2 -= lr * db2

    def keep_weights(self):
        weigths = {
            "W1": self.W1.tolist(),
            "b1": self.b1.tolist(),
            "W2": self.W2.tolist(),
            "b2": self.b2.tolist()
        }
        write_file(weigths, MODEL_DIR, "model.json")

    def get_loss(self):
        return [self.loss, len(self.loss)]

    def train(self, X, y, epochs, lr):
        y = y.reshape(-1, 1)

        # Plot the decision boundary
        x_min, x_max = X[:, 0].min() - .5, X[:, 0].max() + .5
        y_min, y_max = X[:, 1].min() - .5, X[:, 1].max() + .5
        h = .02  # step size in the mesh
        xx, yy = np.meshgrid(np.arange(x_min, x_max, h),
                             np.arange(y_min, y_max, h))
        Z = self.predict(np.c_[xx.ravel(), yy.ravel()])
        Z = Z.reshape(xx.shape)
        plt.contourf(xx, yy, Z, cmap=plt.cm.Spectral)
        plt.scatter(X[:, 0], X[:, 1], c=y.ravel(), cmap=plt.cm.Spectral)
        plt.xlabel("$X_1$")
        plt.ylabel("$X_2$")
        plt.pause(0.1)

        for epoch in range(epochs):
            z1, a1, z2, y_hat = self.feedforward(X)
            dW1, db1, dW2, db2 = self.backpropagation(X, y, z1, a1, z2, y_hat)
            self.update_parameters(dW1, db1, dW2, db2, lr)
            self.keep_weights()
            if epoch % 100 == 0:
                self.loss.append(self.binary_cross_entropy(y, y_hat))
                print(f"Epoch: {epoch}, loss: {self.loss[-1]}")
                # Update decision boundary
                Z = self.predict(np.c_[xx.ravel(), yy.ravel()])
                Z = Z.reshape(xx.shape)
                # Update plot
                plt.clf()
                plt.contourf(xx, yy, Z, cmap=plt.cm.Spectral)
                plt.scatter(X[:, 0], X[:, 1], c=y.ravel(),
                            cmap=plt.cm.Spectral)
                plt.pause(0.1)
                plt.draw()

    def predict(self, x_inputs):
        _, _, _, y_hat = self.feedforward(x_inputs)
        return np.round(y_hat)
