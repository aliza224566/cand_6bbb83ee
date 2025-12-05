def perceptron_epoch(X, y, w, b, lr):
    n_samples = len(X)
    n_features = len(X[0]) if n_samples > 0 else 0

    for i in range(n_samples):
        xi = X[i]
        yi = y[i]

        # compute w·x + b
        dot = sum(w[j] * xi[j] for j in range(n_features)) + b

        # check mistake condition
        if yi * dot <= 0:
            # update weights
            for j in range(n_features):
                w[j] += lr * yi * xi[j]
            # update bias
            b += lr * yi

    return [w, b]
