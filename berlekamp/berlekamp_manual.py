from berlekamp.tools import reverse

def berlekamp_massey_manual(sequence):
    # Первый шаг, задаём начальные данные
    n = len(sequence)
    N = 0
    L = 0
    m = -1
    # Начальные массивы такой же длины, что и входная последовательность
    b = [0 for _ in range(n)]
    t = b.copy()
    c = b.copy()
    b[0] = 1
    c[0] = 1
    # Основной цикл
    while N < n:
        d = 0
        for i in range(L + 1):
            d += c[i] * sequence[N - i]
        d = d % 2
        if d == 1:
            t = c.copy()
            for i in range(N - m, n):
                index1 = i
                index2 = i - (N - m)
                c[index1] = (c[index1] + b[index2]) % 2
            if 2 * L <= N:
                L = N + 1 - L
                m = N
                b = t.copy()
        N += 1
    return reverse(c[:L])
