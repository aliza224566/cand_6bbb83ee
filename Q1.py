def confusion_matrix(y_true, y_pred, labels):
    n = len(labels)
    index = {label: i for i, label in enumerate(labels)}
    cm = [[0]*n for _ in range(n)]

    for t, p in zip(y_true, y_pred):
        if t in index and p in index:
            cm[index[t]][index[p]] += 1

    return cm
