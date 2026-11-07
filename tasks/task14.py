def factorize(n):
    factors = []
    d = 2
    while d * d <= n:
        while n % d == 0:
            factors.append(d)
            n //= d
        d += 1
    if n > 1:
        factors.append(n)
    return factors


def run():
    for n in (15, 21, 91):
        print(f"{n} = " + " x ".join(str(x) for x in factorize(n)))