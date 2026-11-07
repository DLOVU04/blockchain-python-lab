LOG = [
    ("uniswap", 7000),
    ("aave", 5000),
    ("uniswap", 5500),
    ("compound", 4500),
    ("aave", 3500),
]


def aggregate(log):
    totals = {}
    for sg, cnt in log:
        totals[sg] = totals.get(sg, 0) + cnt
    return totals


def run():
    totals = aggregate(LOG)
    for sg, cnt in totals.items():
        print(f"{sg}: {cnt:,} запросов")
    print(f"Самый нагруженный: {max(totals, key=totals.get)}")
    print(f"Всего запросов: {sum(totals.values()):,}")