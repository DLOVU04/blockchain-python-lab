def confirm_time(n, k=1000):
    return k / n


def run():
    for n in (10, 100, 1000):
        print(f"n={n:>4} транзакций -> время подтверждения = {confirm_time(n):.2f} усл.ед.")