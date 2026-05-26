import matplotlib.pyplot as plt

# חיזוי
predictions = model.predict(X)

print("Predictions:")
print(predictions)

print("\nReal labels:")
print(y)

# ציור הנקודות
for i in range(len(X)):

    if y[i] == 0:
        plt.scatter(X[i][0], X[i][1], marker='o')

    else:
        plt.scatter(X[i][0], X[i][1], marker='x')

plt.xlabel("x1")
plt.ylabel("x2")

plt.title("Perceptron AND Dataset")

plt.grid()

plt.show()