def softmax_classify(W, b, X):
    C = len(W)      # classes
    M = len(X)      # samples
    D = len(X[0]) if M > 0 else 0

    preds = []
    for x in X:
        logits = []
        for c in range(C):
            s = sum(W[c][j] * x[j] for j in range(D)) + b[c]
            logits.append(s)
        # argmax with smallest index on ties
        best = max(range(C), key=lambda idx: (logits[idx], -idx))
        preds.append(best)
    return preds
