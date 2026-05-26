import numpy as np

# AND dataset

X = np.array([
    [0, 0],
    [0, 1],
    [1, 0],
    [1, 1]
])

y = np.array([
    0,
    0,
    0,
    1
])

# יצירת מודל
model = Perceptron(
    learning_rate=0.1,
    epochs=20
)

# אימון
model.fit(X, y)

print("Weights:")
print(model.weights)

print("\nBias:")
print(model.bias)