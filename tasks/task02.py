def reads_per_second(writes, low=100, high=10000):
    return writes * low, writes * high


def run():
    writes = 500
    lo, hi = reads_per_second(writes)
    print(f"Записей в секунду: {writes:,}")
    print(f"Минимум чтений/с: {lo:,}")
    print(f"Максимум чтений/с: {hi:,}")