import random


def build_tangle(n=6):
    random.seed(42)
    tangle = []
    for i in range(n):
        if i < 2:
            tangle.append([])
        else:
            tangle.append(random.sample(range(i), 2))
    return tangle


def run():
    for i, parents in enumerate(build_tangle()):
        if not parents:
            print(f"Транзакция {i} подтверждает: — (начальная)")
        else:
            print(f"Транзакция {i} подтверждает: {parents}")