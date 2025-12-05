def bow_transform(corpus, vocab):
    vocab_index = {term: i for i, term in enumerate(vocab)}
    out = []

    for doc in corpus:
        tokens = doc.split()          # whitespace tokenization
        counts = [0] * len(vocab)

        for tok in tokens:
            if tok in vocab_index:    # ignore tokens not in vocab
                counts[vocab_index[tok]] += 1

        out.append(counts)

    return out
