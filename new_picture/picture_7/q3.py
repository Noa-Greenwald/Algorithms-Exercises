import numpy as np
from sklearn.datasets import load_breast_cancer

def print_stats(X, feature_names, title):
    print("\n" + "=" * 60)
    print(title)
    print("=" * 60)

    for i in range(X.shape[1]):
        col = X[:, i]
        mean = np.mean(col)
        std = np.std(col)

        print(f"{feature_names[i]:30s} mean = {mean:.6f} | std = {std:.6f}")


def normalize(X):
    means = np.mean(X, axis=0)
    stds = np.std(X, axis=0)

    # מניעת חלוקה באפס
    stds[stds == 0] = 1

    X_norm = (X - means) / stds
    return X_norm


def main():
    # ── Load Wisconsin dataset ─────────────────────────────
    data = load_breast_cancer()
    X = data.data
    feature_names = data.feature_names

    # ── 1. Before normalization ────────────────────────────
    print_stats(X, feature_names, "BEFORE NORMALIZATION")

    # ── 2. Normalization (Z-score) ─────────────────────────
    X_norm = normalize(X)

    # ── 3. After normalization ─────────────────────────────
    print_stats(X_norm, feature_names, "AFTER NORMALIZATION")


if __name__ == "__main__":
    main()