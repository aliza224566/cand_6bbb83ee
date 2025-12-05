def top_k_cosine(query, docs, k):
    import math

    def dot(a, b):
        return sum(x*y for x, y in zip(a, b))

    def norm(v):
        return math.sqrt(sum(x*x for x in v))

    qn = norm(query)
    sims = []

    for i, d in enumerate(docs):
        dn = norm(d)
        if qn == 0 or dn == 0:
            sim = 0
        else:
            sim = dot(query, d) / (qn * dn)
        sims.append((sim, i))

    # sort: highest similarity first, tie → smaller index
    sims.sort(key=lambda x: (-x[0], x[1]))

    return [idx for (_, idx) in sims[:k]]
