def standardize_columns(X):
    if not X:
        return []

    rows, cols = len(X), len(X[0])
    out = [[0]*cols for _ in range(rows)]

    for j in range(cols):
        col = [X[i][j] for i in range(rows)]
        mean = sum(col) / rows
        var = sum((x - mean)**2 for x in col) / rows  # population variance
        std = var ** 0.5

        if std == 0:
            for i in range(rows):
                out[i][j] = 0.0
        else:
            for i in range(rows):
                z = (X[i][j] - mean) / std
                out[i][j] = round(z, 4)

    return out
