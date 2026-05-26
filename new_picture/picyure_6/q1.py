import numpy as np


class Perceptron:

    def __init__(self, learning_rate=0.1, epochs=10):

        self.learning_rate = learning_rate
        self.epochs = epochs

    def activation(self, x):

        if x >= 0:
            return 1
        else:
            return 0

    def fit(self, X, y):

        n_samples, n_features = X.shape

        # אתחול משקלים
        self.weights = np.zeros(n_features)

        # bias
        self.bias = 0

        # אימון
        for epoch in range(self.epochs):

            for i in range(n_samples):

                linear_output = np.dot(X[i], self.weights) + self.bias

                prediction = self.activation(linear_output)

                error = y[i] - prediction

                # עדכון משקלים
                self.weights += self.learning_rate * error * X[i]

                # עדכון bias
                self.bias += self.learning_rate * error

    def predict(self, X):

        linear_output = np.dot(X, self.weights) + self.bias

        predictions = []

        for value in linear_output:
            predictions.append(self.activation(value))

        return np.array(predictions)