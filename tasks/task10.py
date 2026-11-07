TRANSACTIONS = [
    ("Alice", "Bob", 50),
    ("Bob", "Alice", 20),
    ("Alice", "Carol", 10),
]


def filter_and_balance(txs, addr):
    selected = [t for t in txs if t[0] == addr or t[1] == addr]
    balance = sum(a for f, t, a in txs if t == addr) - sum(a for f, t, a in txs if f == addr)
    return selected, balance


def run():
    addr = "Alice"
    selected, balance = filter_and_balance(TRANSACTIONS, addr)
    print(f"Транзакции {addr} ({len(selected)}):")
    for f, t, a in selected:
        print(f"  {f} -> {t}: {a}")
    print(f"Баланс {addr}: {balance}")